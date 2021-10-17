from django.shortcuts import render, redirect, get_object_or_404
from Support.code.apps._asks import user_permission
from Support.code.apps._asks.settings import verify_process__settings, create_theme, try_update_for_admin
from Support.code.apps._asks.ask import register_question, validate_question, verify_process__ask, delete_question
from Support.code.apps._asks import send_errors_of_asks
from Support.code.validators import validate_unique
from room.models import Room, Theme
from django.contrib import messages


BP = 'apps/asks' # base path


def ask(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    
    context = dict()
    context['code'] = code
    context['username'] = request.session['main']['username']
    context['themes'] = Room.objects.get(code=code).themes.filter(active=True)
    context['my_questions'] = request.session['main']['my_questions']
    
    # main flow
    if request.method == 'POST':
        process = verify_process__ask(request)
        
        if process['action'] == 'register_question':
            operation = validate_question(request)
            if operation['response'] == 'success':
                register_question(request, code)
                messages.success(request, 'Questão criada com sucesso')
            else:        
                send_errors_of_asks(request, operation['errors'])

        elif process['action'] == 'delete_question':
            delete_question(request, code)
    
    
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
    context['themes'] = Room.objects.get(code=code).themes.filter(active=True)
    
    # main flow
    # context['questions'] = get_questions_by_themes()
    
    return render(request, f'{BP}/records.html', context)



def settings_view(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    
    context = dict()
    context['code'] = code
    # main flow
    if request.method == 'POST':
        process = verify_process__settings(request)
        if process['action'] == 'create theme':
            create_theme(request, code)
        elif process['action'] == 'update for admin':
            try_update_for_admin(request, code)
            
    # end flow
    context['admin'] = request.session['main']['admin']
    context['themes'] = Room.objects.get(code=code).themes.all()
            
    return render(request, f'{BP}/settings.html', context)


