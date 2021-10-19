from Support.code.utils import filters
from Support.code.checks import check_null
from room.models import Theme, Room
from django.contrib import messages


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

    new_theme = Theme.objects.create(name=theme, creator=user, active=True)
    new_theme.save()
    
    current_room = Room.objects.get(code=code)
    current_room.themes.add(new_theme)


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
    