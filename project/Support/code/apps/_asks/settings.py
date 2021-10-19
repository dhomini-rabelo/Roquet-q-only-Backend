from Support.code.utils import filters
from Support.code.checks import check_null
from Support.code.core import get_post_form_errors
from room.models import Theme, Room
from django.contrib import messages
from .._room import send_errors_of_room


def validate_theme_form(request):
    theme = filters(request.POST.get('theme'))
    
    fv = [
        [theme, 'str', 'theme', [('max_length', 128), ('min_length', 10)]],
    ] 

    form_errors = get_post_form_errors(fv)
    
    if form_errors is None:
        return {'status': 'valid'}
    else:
        return {'status': 'invalid', 'errors': form_errors}


def verify_process__settings(request):
    rp = request.POST
    action = filters(rp.get('action'))
    
    values = {'add': 'create theme', 'disable': 'disable theme', 'change': 'update for admin'}
    
    if not check_null(action):
        return {'action': values[action]}
    else: 
        return {'action': 'none'}
    

def create_theme(request, code):
    theme, user = filters(request.POST.get('theme')), request.session['main']['username']
    validation = validate_theme_form(request)

    if validation['status'] == 'valid': 
        new_theme = Theme.objects.create(name=theme, creator=user, active=True)
        new_theme.save()
        current_room = Room.objects.get(code=code)
        current_room.themes.add(new_theme)
    else:
        send_errors_of_room(request, validation['errors'])


def disable_theme(request, code):
    theme_name = filters(request.POST.get('theme'))
    
    themes = Room.objects.get(code=code).themes.filter(active=True)
    theme = themes.get(name=theme_name)
    theme.active = False
    theme.save()
    
    
def try_update_for_admin(request, code):
    admin_password = Room.objects.get(code=code).password_admin
    password = filters(request.POST.get('password'))
    
    if admin_password == password:
        request.session['main']['admin'] = True
        messages.success(request, 'Agora você é administrador')
    else:
        messages.error(request, 'Senha de administrador incorreta')
    