from room.models import Room
from random import randint
from Support.code.core import get_post_form_errors
from Support.code.utils import filters
from Support.code.validators import validate_unique


def get_room_code():
    code = randint(100000, 999999)
    while not validate_unique(Room, 'code', code):
        code = randint(100000, 999999)
    return code


def create_an_room(request):
    rp = request.POST
    
    username, password, code = filters(rp.get('username')), filters(rp.get('password')), rp.get('code') 

    fv = [
        [username, 'str', 'username', []],
        [password, 'str', 'password', [('caracters', True, True), ('min_length', 4), ('max_length', 128)]],
        [code, 'int', 'code', [('unique', 'code', 'int'), ('equal_length', 6)]],
    ]  # form validation
    
    form_errors = get_post_form_errors(fv, Room)
    
    if form_errors is None:
        new_room = Room.objects.create(creator=username, code=code, password_admin=password)
        new_room.save()
        return {'status': 'success'}
    else:
        return form_errors | {'status': 'error'}

