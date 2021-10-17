from django.contrib import messages



def send_errors_of_asks(request, errors: dict):
    for field, error_message in errors.items():
        if error_message == 'Não está em uso':
            messages.error(request, 'Não existe')
        elif field != 'status':
            message_name = {'username': 'O username', 'question': 'A pergunta', 'theme': 'O tema'}
            messages.error(request, error_message.replace('Este campo', message_name[field]))
            
            
            
def user_permission(request):
    user_data = request.session.get('main')
    if user_data is None:
        return False
    else:
        return True
