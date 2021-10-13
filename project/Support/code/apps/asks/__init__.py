
def user_permission(request):
    user_data = request.session.get('main')
    if user_data is None:
        return False
    else:
        return True
    