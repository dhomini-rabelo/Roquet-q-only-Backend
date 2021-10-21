from django.shortcuts import render, redirect, get_object_or_404
from Support.code.apps._asks import user_permission
from Support.code.apps._asks.settings import verify_process__settings, create_theme, try_update_for_admin, disable_theme
from Support.code.apps._asks.records import get_questions_answered, get_questions_for_end_rank
from Support.code.apps._asks.ask import register_question, validate_question, verify_process__ask, delete_question
from Support.code.apps._asks import send_errors_of_asks
from Support.code.apps._asks.vote import select_questions, register_vote, get_best_questions, save_questions_for_vote
from Support.code.validators import validate_unique
from room.models import Room
from django.contrib import messages
import time


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
    request.session['main']['questions_saved_to_vote'] = None
    
    # main flow
    if request.method == 'POST':
        process = verify_process__ask(request)
        
        if process['action'] == 'register_question':
            operation = validate_question(request, code)
            if operation['response'] == 'valid':
                register_question(request, code)
                messages.success(request, 'Questão criada com sucesso')
            elif operation['response'] == 'invalid':        
                send_errors_of_asks(request, operation['errors'])
                
                
        elif process['action'] == 'delete_question':
            delete_question(request)
            
        return redirect('ask', code)
    
    
    return render(request, f'{BP}/ask.html', context)



def vote(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    
    context = dict()
    context['code'] = code
    
    # main flow
    if request.method == 'GET':
        context['themes'] = Room.objects.get(code=code).themes.filter(active=True)
        context['questions_for_ranking'] = get_best_questions(code)
        context['questions_for_vote'] = select_questions(request, context['themes'])
        request.session['main']['questions_saved_to_vote'] = save_questions_for_vote(context['questions_for_vote'])

            
        
    elif request.method == 'POST':
        register_vote(request, code)
        return redirect('vote', code) 


    return render(request, f'{BP}/vote.html', context)



def records_view(request, code):
    # initial flow
    if not user_permission(request):
        return redirect('enter_room')
    
    context = dict()
    context['code'] = code
    context['themes'] = Room.objects.get(code=code).themes.filter(active=False)
    
    # main flow
    context['answered'] = get_questions_answered(context['themes'])
    context['questions_for_ranking'] = get_questions_for_end_rank(context['themes'])
    context['admin'] = request.session['main']['admin']
    
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
        elif process['action'] == 'disable theme':
            disable_theme(request, code)
        elif process['action'] == 'update for admin':
            try_update_for_admin(request, code)
        
        return redirect('settings', code)
        
            
    # end flow
    context['admin'] = request.session['main']['admin']
    context['active_themes'] = Room.objects.get(code=code).themes.filter(active=True)
    context['disabled_themes'] = Room.objects.get(code=code).themes.filter(active=False)
            
    return render(request, f'{BP}/settings.html', context)


