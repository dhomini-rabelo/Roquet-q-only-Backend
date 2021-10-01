from django.shortcuts import render

BP = 'apps/room' # base path


def home(request):
    return render(request,f'{BP}/home.html')


def create_room(request):
    return render(request, f'{BP}/create_room.html')


def enter_room(request):
    return render(request, f'{BP}/enter_room.html')