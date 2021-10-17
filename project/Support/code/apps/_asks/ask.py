from Support.code.utils import filters
from Support.code.core import get_post_form_errors
from . import send_errors_of_asks
from room.models import Theme, Room
from asks.models import Question
from django.contrib import messages
from datetime import datetime


def validate_question(request):
    rp = request.POST
    
    username, question = filters(rp.get('username')), filters(rp.get('question'))
    theme = filters(rp.get('theme'))
    
    fv = [
        [username, 'str', 'username', []],
        [question, 'str', 'question', []],
        [theme, 'str', 'theme', [('exists', 'name')]],
    ]
    
    form_errors = get_post_form_errors(fv, Theme)
    
    if form_errors is None:
        return {'response': 'success'}
    else:
        return {'response': 'fail', 'errors': form_errors} 
    


def register_question(request, code):
    # main flow
    rp = request.POST
    username, question = filters(rp.get('username')), filters(rp.get('question'))
    theme = filters(rp.get('theme'))
    
    new_question = Question(creator=username, text=question, answered=False,
                            up_votes=0, down_votes=0)
    new_question.save()
    
    room = Room.objects.get(code=code)
    theme_of_room = room.themes.get(name=theme)
    theme_of_room.questions.add(new_question)
    
    # end flow
    question = {
        'text': question, 'horary': new_question.creation.strftime('%H:%M'),
        'theme': theme, 'order': len(request.session['main']['my_questions'])
    }
    request.session['main']['my_questions'].append(question)
     
     
