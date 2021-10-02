from Support.code.checks import check_null
from Support.code.validators import validate_caracters


def create_main_session(request, admin=False):
    rp = request.POST
    username = rp.get('username')
    if check_null(username):
        request.session['main'] = {'username': username, 'admin': admin}