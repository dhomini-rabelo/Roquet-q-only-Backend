from django.shortcuts import render
from Support.code.apps.room.create_room import get_room_code, create_other_room
from Support.code.apps.room.enter_room import create_main_session
from .models import Room


BP = 'apps/room' # base path



def home(request):
    return render(request,f'{BP}/home.html')



def create_room(request):
    context = dict()
        
    if request.method == 'POST':
        create_other_room(request)
        create_main_session(request, True)
        
    context['code'] = get_room_code()
    
    return render(request, f'{BP}/create_room.html', context)



def enter_room(request):
    if request.method == 'POST':
        create_main_session(request)
    return render(request, f'{BP}/enter_room.html')



def code_room(request, code):
    context = dict()
    context['code'] = code
    if request.method == 'POST':
        create_main_session(request)
    return render(request, f'{BP}/code_room.html', context)