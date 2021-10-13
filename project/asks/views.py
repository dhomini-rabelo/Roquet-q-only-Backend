from django.shortcuts import render, redirect, get_object_or_404
from Support.code.apps.asks import user_permission
from room.models import Room


BP = 'apps/asks' # base path


def ask(request, code):
    # initial flow
    context = dict()
    context['code'] = code
    if not user_permission(request):
        return redirect('enter_room')
    
    # main flow
    return render(request, f'{BP}/ask.html', context)



def vote(request, code):
    # initial flow
    context = dict()
    context['code'] = code
    if not user_permission(request):
        return redirect('enter_room')
    
    # main flow
    return render(request, f'{BP}/vote.html', context)



def records_view(request, code):
    # initial flow
    context = dict()
    context['code'] = code
    if not user_permission(request):
        return redirect('enter_room')
    
    # main flow
    return render(request, f'{BP}/records.html', context)



def settings_view(request, code):
    # initial flow
    context = dict()
    context['code'] = code
    context['admin'] = request.session['main']['admin']
    if not user_permission(request):
        return redirect('enter_room')
    
    # main flow
    return render(request, f'{BP}/settings.html', context)