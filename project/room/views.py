from django.shortcuts import render
from random import randint


BP = 'apps/room' # base path


def home(request):
    return render(request,f'{BP}/home.html')


def create_room(request):
    context = dict()
        
    if request.method != 'POST':
        context['code'] = randint(100000, 999999)
    
    rp = request.POST
    username, title = rp.get('username'), rp.get('title')
    password, code = rp.get('password'), rp.get('code')
    
    return render(request, f'{BP}/create_room.html', context)


def enter_room(request):
    return render(request, f'{BP}/enter_room.html')


