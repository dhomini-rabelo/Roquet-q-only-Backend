from django.contrib import admin
from .models import Question, Survey, Option



@admin.register(Option)
class OptionInline(admin.ModelAdmin):
    list_display = 'text', 'votes', 'correct'
    list_display_links = 'text',


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = 'creator', 'creation', 'finalized'
    list_display_links = 'creator',


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'creator', 'creation', 'answered'
    list_display_links = 'creator',

