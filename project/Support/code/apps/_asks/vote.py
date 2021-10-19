from random import randint, shuffle
from Support.code.utils import filters
from asks.models import Question
from room.models import Room


# support functions
def select_items(obj: list, quantity=3):
    if len(obj) < quantity:
        return obj
    
    selecteds = []
    
    while len(selecteds) < quantity:
        selected = randint(0, len(obj) - 1)
        if selected not in selecteds:
            selecteds.append(selected)
    
    return [obj[number] for number in selecteds]
        
        
# main functions

def select_questions(request, themes, post=False):
    if not post:
        get_questions = lambda theme: theme.questions.exclude(creator=request.session['main']['username'], answered=False)
        sets_of_questions = map(get_questions, themes)
    else:
        get_questions_by_id = lambda id_list: [Question.objects.get(id=id) for id in id_list]
        sets_of_questions = map(get_questions_by_id, themes)
    
    
    new_sets = []

    for set_questions in list(sets_of_questions):
        question_group = []
        for question in set_questions:
            if question.id not in request.session['main']['voted_questions'] and question.answered == False:
                question_group.append(question)
                        
        new_sets.append(select_items(question_group, 5))
    
    return new_sets    


    
    
    
def register_vote(request, code):
    # main flow
    rp = request.POST
    text, theme, action = filters(rp.get('text')), filters(rp.get('theme')), filters(rp.get('action'))
    
    room = Room.objects.get(code=code)
    theme_of_room = room.themes.get(name=theme)
    question = theme_of_room.questions.get(text=text)
     
    
    if action == 'up' and question.id not in request.session['main']['voted_questions']:
        question.up_votes += 1
    elif action == 'down' and question.id not in request.session['main']['voted_questions']:
        question.down_votes += 1
    elif action == 'mark' and request.session['main']['admin']:
        question.answered = True
    
    question.update_score()
    question.save()
    
    # end flow
    
    request.session['main']['voted_questions'].append(question.id)
    
        
        
def get_best_questions(code):
    best_questions = []
    
    room = Room.objects.get(code=code)
    themes_of_room = room.themes.all()
    
    for theme in themes_of_room:
        questions = theme.questions.order_by('-score')
        if len(questions) >= 5:
            best_questions.append(questions[:5])
        else:
            best_questions.append(questions)
    
    return best_questions
        
        
        
def save_questions_for_vote(questions):
    get_id_questions = lambda questions_list: [question.id for question in questions_list]
    save = map(get_id_questions, questions)
    
    return list(save)