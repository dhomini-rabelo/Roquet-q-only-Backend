from django.contrib import admin
from .models import Question, Survey, Option


#* FOR COLUMNS


def get_theme(object):
    theme = object.theme_set.all().first()
    if theme is None:
        return '[ NONE ]'
    else:
        return theme.name


#* ADMIN SETTINGS


@admin.register(Option)
class OptionInline(admin.ModelAdmin):
    list_display = 'get_creator', 'text', 'votes', 'correct'
    list_display_links = 'text',
    list_per_page = 20
    
    @admin.display(description='creator')    
    def get_creator(self, object):
        survey = object.survey_set.all().first()
        if survey is None:
            return '[ NONE ]'
        return survey.creator       


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = 'id', 'get_theme_of_survey', 'creator', 'creation', 'finalized'
    list_display_links = 'creator',
    list_per_page = 20
    
    @admin.display(description='theme')    
    def get_theme_of_survey(self, object):
        return get_theme(object)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'id', 'get_theme_of_question', 'creator', 'creation', 'answered'
    list_display_links = 'creator',
    list_per_page = 20

    @admin.display(description='theme')    
    def get_theme_of_question(self, object):
        return get_theme(object)
    
    
    
