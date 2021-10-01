from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.fields.related import ManyToManyField
from asks.models import Question, Survey

class Theme(Model):
    name = CharField(max_length=128)
    question = ManyToManyField(Question)
    polls = ManyToManyField(Survey) 
    
    
class Room(Model):
    title = CharField(max_length=128)
    creator = CharField(max_length=128)
    code = PositiveIntegerField()
    themes = ManyToManyField(Theme)
    password_admin = CharField(max_length=128)