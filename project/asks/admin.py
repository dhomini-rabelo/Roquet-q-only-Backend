from django.contrib import admin
from .models import Question


#* ADMIN SETTINGS

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'room', 'theme', 'creator', 'get_text', 'score', 'answered',  'id'
    list_display_links = 'creator',
    list_per_page = 20
    
    def room(self, question):
        return str(question.theme.room.code)
    
    @admin.display(description='question')
    def get_text(self, question):
        text_of_question = question.text
        return text_of_question
        
    def score(self, question):
        return str(question.up_votes - question.down_votes)
        
    
    
    
