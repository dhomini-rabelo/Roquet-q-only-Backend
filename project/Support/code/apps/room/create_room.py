from room.models import Room
from random import randint


def get_room_code():
    code = randint(100000, 999999)
    while code in Room.objects.values_list('code'):
        code = randint(100000, 999999)
    return code


def create_room(request):
    rp = request.POST
    username, title = rp.get('username'), rp.get('title')
    password, code = rp.get('password'), rp.get('code') 
    Room.objects.create(title=title, creator=username, code=code, admin_password=password)