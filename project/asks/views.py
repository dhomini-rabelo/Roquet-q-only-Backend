from django.shortcuts import render, redirect, get_object_or_404
from Support.code.apps._asks import user_permission
from Support.code.apps._asks.settings import verify_settings_proccess, create_theme, try_update_for_admin
from room.models import Room


BP = 'apps/asks' # base path


def ask(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    context = dict()
    context['code'] = code
    context['username'] = request.session['main']['username']
    
    
    # main flow
    return render(request, f'{BP}/ask.html', context)



def vote(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    context = dict()
    context['code'] = code
    
    # main flow
    return render(request, f'{BP}/vote.html', context)



def records_view(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    context = dict()
    context['code'] = code
    
    # main flow
    return render(request, f'{BP}/records.html', context)



def settings_view(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    context = dict()
    context['code'] = code
    # main flow
    if request.method == 'POST':
        proccess = verify_settings_proccess(request)
        if proccess['action'] == 'create theme':
            create_theme(request, code)
        elif proccess['action'] == 'update for admin':
            try_update_for_admin(request, code)
            
    # end flow
    context['admin'] = request.session['main']['admin']
            
    return render(request, f'{BP}/settings.html', context)