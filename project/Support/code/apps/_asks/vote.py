from random import randint, shuffle
from Support.code.utils import filters
from asks.models import Question
from room.models import Room
from django.db.models import Q

# support functions
def select_items(obj: list, quantity=3):
    if len(obj) <= quantity:
        return obj
    
    selecteds = []
    
    while len(selecteds) < quantity:
        selected = randint(0, len(obj) - 1)
        if selected not in selecteds:
            selecteds.append(selected)
    
    return [obj[number] for number in selecteds]
        

def get_questions_by_id(request, id_list):
    my_questions = [question['text'] for question in request.session['main']['my_questions']]
    questions = []
    
    question = Question.objects.get(id=id_list[0])
    theme = question.theme_set.first() 
    
    if theme is not None and theme.active == True:
        for id in id_list:
            question = Question.objects.get(id=id)
            if question.answered == False and id not in request.session['main']['voted_questions']:
                questions.append(question)


        if len(questions) < 5 and len(theme.questions.exclude(Q(text__in=my_questions) | Q(answered=True))) > 6:
            for question in theme.questions.exclude(Q(text__in=my_questions) | Q(answered=True)):
                if question.id not in request.session['main']['voted_questions'] and question not in questions:
                    questions.append(question)
                    if len(questions) == 5:
                        break
            
    return questions


def regulate_sets(request, sets_of_questions, themes):
    my_questions = [question['text'] for question in request.session['main']['my_questions']]
    regulated_sets = [set_questions for set_questions in sets_of_questions if set_questions != []]
    if not len(regulated_sets) == len(themes):
        saved_themes = [set_questions[0].theme_set.first() for set_questions in regulated_sets]
        for theme in themes:
            if theme not in saved_themes:
                new_questions = theme.questions.exclude(text__in=my_questions)
                regulated_sets.append(select_items(new_questions, 5))
    
    return regulated_sets
            



# main functions

def select_questions(request, themes):
    my_questions = [question['text'] for question in request.session['main']['my_questions']]
    if request.session['main'].get('questions_saved_to_vote') is None:
        get_questions = lambda theme: theme.questions.exclude(Q(text__in=my_questions) | Q(answered=True))
        sets_of_questions = [list(get_questions(theme)) for theme in themes]
        new_sets = []

        for set_questions in sets_of_questions:                            
            new_sets.append(select_items(set_questions, 5))

        return new_sets    
    else:
        sets_of_questions = [get_questions_by_id(request, id_list) for id_list in request.session['main']['questions_saved_to_vote']]
        sets_of_questions = regulate_sets(request, sets_of_questions, themes)
        return sets_of_questions     
    
    
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
    themes = Room.objects.get(code=code).themes.only('questions', 'active').filter(active=True)
    
    for theme in themes:
        questions = theme.questions.exclude(answered=True).order_by('-score')
        if questions.count() >= 5:
            best_questions.append(questions[:5])
        else:
            best_questions.append(questions)
    
    return best_questions
        
        
        
def save_questions_for_vote(questions):
    get_id_questions = lambda questions_list: [question.id for question in questions_list]
    save = map(get_id_questions, questions)
    
    return list(save)