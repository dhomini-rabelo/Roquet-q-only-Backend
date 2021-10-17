from Support.code.core import get_post_form_errors
from Support.code.utils import filters
from room.models import Room



def validate_room_entry(request):
    rp = request.POST
    
    username, code = filters(rp.get('username')),  rp.get('code') 

    fv = [
        [username, 'str', 'username', []],
        [code, 'int', 'code', [('equal_length', 6)]],
    ]
    
    form_errors = get_post_form_errors(fv, Room)
    
    if form_errors is None:
        return {'status': 'success'}
    else:
        return form_errors | {'status': 'error'}



def create_main_session(request, admin=False):
    username = request.POST.get('username')
    request.session['main'] = {'username': username, 'admin': admin, 'my_questions': []}
