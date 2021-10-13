from django.shortcuts import redirect, render
from Support.code.apps.room.create_room import get_room_code, create_an_room, send_errors_of_room
from Support.code.apps.room.enter_room import create_main_session, validate_room_entry
from .models import Room


BP = 'apps/room' # base path



def home(request):
    return render(request,f'{BP}/home.html')



def create_room(request):
        
    context = dict()
    context['code'] = get_room_code()

    if request.method == 'POST':
        response = create_an_room(request)
        if response['status'] == 'success':
            # create_main_session(request, admin=True)
            return redirect('settings', request.POST.get('code'))
        else:
            send_errors_of_room(request, response)
            
    return render(request, f'{BP}/create_room.html', context)



def enter_room(request):
    if request.method == 'POST':
        response = validate_room_entry(request)
        if response['status'] == 'success':
            create_main_session(request, admin=False)
            return redirect('ask', request.POST.get('code'))
        else:
            send_errors_of_room(request, response)
        
    return render(request, f'{BP}/enter_room.html')



def code_room_shortcut(request, code):
    context = dict()
    context['code'] = code
    
    if request.method == 'POST':
        response = validate_room_entry(request)
        if response['status'] == 'success':
            create_main_session(request, admin=False)
            return redirect('ask', request.POST.get('code'))
        else:
            send_errors_of_room(request, response)
            
    return render(request, f'{BP}/code_room.html', context)