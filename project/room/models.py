from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)
from django.db.models.fields.related import ManyToManyField
from asks.models import Question


class Theme(Model):
    creator = CharField(max_length=128, default='')
    name = CharField(max_length=128)
    questions = ManyToManyField(Question, blank=True)
    active = BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Room(Model):
    creator = CharField(max_length=128, default='')
    code = PositiveIntegerField(unique=True)
    themes = ManyToManyField(Theme, blank=True)
    password_admin = CharField(max_length=128)

    def __str__(self):
        return str(self.code)
