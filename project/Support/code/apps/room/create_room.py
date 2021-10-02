from room.models import Room
from random import randint
from Support.code.core import get_post_form_errors
from Support.code.checks import check_null
from Support.code.utils import filters


def get_room_code():
    code = randint(100000, 999999)
    while code in Room.objects.values_list('code'):
        code = randint(100000, 999999)
    return code


def create_other_room(request):
    rp = request.POST
    
    username, title = filters(rp.get('username'), 'strip'), filters(rp.get('title'), 'name')
    password, code = filters(rp.get('password'), 'strip'), rp.get('code')
    
    fv = [
        [username, 'pass', 'username', []],
        [title, 'pass', 'title', []],
        [password, 'pass', 'password', [('caracters', True, True), ('min_length', 4)]],
        [code, 'int', 'code', [('unique', 'code'), ('equal_length', 6)]],
    ]  # form validation
    
    form_errors = get_post_form_errors(fv, Room)
    
    if form_errors is None:
        print('oi')
        # new_room = Room.objects.create(title=title, creator=username, code=code, admin_password=password)
        # new_room.save()
    else:
        print('olá')
        request.session['errors'] = {}
    print(form_errors)
    