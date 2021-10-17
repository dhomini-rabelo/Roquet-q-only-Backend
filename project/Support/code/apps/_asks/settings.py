from Support.code.utils import filters
from Support.code.checks import check_null
from room.models import Theme, Room
from django.contrib import messages


def verify_settings_proccess(request):
    rp = request.POST
    theme, password = filters(rp.get('theme')), filters(rp.get('password'))
    
    if not check_null(theme):
        return {'action': 'create theme'}
    elif not check_null(password):
        return {'action': 'update for admin'}
    else: 
        return {'action': 'none'}
    

def create_theme(request, code):
    theme, user = filters(request.POST.get('theme')), request.session['main']['username']

    new_theme = Theme.objects.create(name=theme, creator=user, active=True)
    new_theme.save()
    
    current_room = Room.objects.get(code=code)
    current_room.themes.add(new_theme)
    
    
def try_update_for_admin(request, code):
    admin_password = Room.objects.get(code=code).password_admin
    password = filters(request.POST.get('password'))
    
    if admin_password == password:
        request.session['main']['admin'] = True
        messages.success(request, 'Agora você é administrador')
    else:
        messages.error(request, 'Senha de administrador incorreta')
    