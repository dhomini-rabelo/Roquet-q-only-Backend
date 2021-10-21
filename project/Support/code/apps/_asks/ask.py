from Support.code.utils import filters
from Support.code.core import get_post_form_errors
from Support.code.validators import validate_unique
from . import send_errors_of_asks
from room.models import Theme, Room
from asks.models import Question
from django.contrib import messages
from datetime import datetime
from datetime import timedelta


# support functions

def exists_question(question, theme, code):
    room = Room.objects.get(code=code)
    theme_of_room = room.themes.get(name=theme)
    
    questions = list(item[0] for item in theme_of_room.questions.values_list('text'))
    
    if question in questions:
        return True
    return False


def verify_process__ask(request):
    allowed_process = ['delete_question', 'register_question']

    process = request.POST.get('process')
    
    if isinstance(process, str) and process in allowed_process:
        return {'action': process}                
    else:
        return {'action': 'none'}            


# main functions

def validate_question(request, code):
    rp = request.POST
    
    username, question = filters(rp.get('username')), filters(rp.get('question'))
    theme = filters(rp.get('theme'))
    
    fv = [
        [username, 'str', 'username', [('max_length', 128)]],
        [question, 'str', 'question', [('max_length', 400)]],
        [theme, 'str', 'theme', [('exists', 'name')]],
    ]
    
    form_errors = get_post_form_errors(fv, Theme)
    
    if exists_question(question, theme, code):
        return {'response': 'invalid', 'errors': 'Esta pergunta já foi cadastrada'}
    elif form_errors is None:
        return {'response': 'valid'}
    else:
        return {'response': 'invalid', 'errors': form_errors} 
    


def register_question(request, code):
    # main flow
    rp = request.POST
    username, question = filters(rp.get('username')), filters(rp.get('question'))
    theme = filters(rp.get('theme'))

    new_question = Question.objects.create(creator=username, text=question, answered=False,
                            up_votes=0, down_votes=0, score=0)
    new_question.save()
    
    theme_of_question = Room.objects.get(code=code).themes.get(name=theme)
    theme_of_question.questions.add(new_question)
    
    # end flow
    horary = new_question.creation - timedelta(hours=3)

    question = {
        'text': question, 'horary': horary.strftime('%H:%M'),
        'theme': theme, 'order': len(request.session['main']['my_questions'])
    }
    
    request.session['main']['my_questions'].insert(0, question)

        
        
        
def delete_question(request):
    rp = request.POST
    
    creator, text = filters(rp.get('creator')), filters(rp.get('text'))
    order = filters(rp.get('order'))
    
    question = Question.objects.get(creator=creator, text=text)
    question.delete()
     
    # end flow
    for key, my_question in enumerate(request.session['main']['my_questions']):
        if my_question['order'] == int(order):
            request.session['main']['my_questions'].pop(key)
            break
