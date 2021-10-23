from django.db.models import F


def get_questions_answered(themes):
    response = []
    
    for theme in themes:
        response.append(theme.questions.filter(answered=True).order_by('creation'))
        
    return response
        

def get_questions_for_end_rank(themes):
    questions = []

    for theme in themes:
        questions.append(theme.questions.annotate(score=F('up_votes')-F('down_votes')).order_by('-score'))
        
    return questions