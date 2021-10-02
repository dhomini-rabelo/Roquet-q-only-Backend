

def create_main_session(request, admin=False):
    rp = request.POST
    username = rp.get('username')
    request.session['main'] = {'username': username, 'admin': admin}