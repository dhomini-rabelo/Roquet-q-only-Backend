from room.models import Theme
from django.db.models import Count


def get_questions_by_themes(themes):
    response = dict()
    
    for theme in themes:
        response[theme.name] = theme.questions.order_by('score')
        
        