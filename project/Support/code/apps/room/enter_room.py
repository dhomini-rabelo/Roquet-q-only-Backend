

def create_main_session(request, admin=False):
    username = request.POST.get('username')
    request.session['main'] = {'username': username, 'admin': admin}
