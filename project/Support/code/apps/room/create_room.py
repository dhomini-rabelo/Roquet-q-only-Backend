from room.models import Room
from random import randint
from Support.code.core import get_post_form_errors
from Support.code.checks import check_null


def get_room_code():
    code = randint(100000, 999999)
    while code in Room.objects.values_list('code'):
        code = randint(100000, 999999)
    return code


def create_other_room(request):
    rp = request.POST
    username, title = rp.get('username'), rp.get('title')
    password, code = rp.get('password'), rp.get('code')
    
    fv = [
        [username, 'pass', 'username', []],
        [title, 'pass', 'título', []],
        [password, 'pass', 'senha', []],
        [code, 'int', 'código', [('unique', 'code')]],
    ]  # form validation
    
    form_errors = get_post_form_errors(fv, Room)
    
    if form_errors is None:
        new_room =Room.objects.create(title=title, creator=username, code=code, admin_password=password)
        new_room.save()
    else:
        request.session['errors'] = {}
    