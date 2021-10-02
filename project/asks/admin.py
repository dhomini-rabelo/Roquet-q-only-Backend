from django.contrib import admin
from .models import Question, Survey, Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'username', 'answered', 'alteration'
    list_display_links = 'username',


@admin.register(Option)
class OptionInline(admin.ModelAdmin):
    list_display = 'text', 'percent', 'correct'
    list_display_links = 'text',


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = 'creator', 'finalized'
    list_display_links = 'creator',


