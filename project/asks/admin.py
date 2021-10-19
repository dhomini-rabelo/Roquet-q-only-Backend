from django.contrib import admin
from .models import Question


#* FOR COLUMNS


def get_theme(object):
    theme = object.theme_set.all().first()
    if theme is None:
        return '[ NONE ]'
    else:
        return theme.name


#* ADMIN SETTINGS


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'id', 'get_theme_of_question', 'creator', 'creation', 'score','answered'
    list_display_links = 'creator',
    list_per_page = 20

    @admin.display(description='theme')    
    def get_theme_of_question(self, object):
        return get_theme(object)
    
    
    
