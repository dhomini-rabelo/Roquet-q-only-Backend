from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)


class Question(Model):
    username = CharField(max_length=128)
    text = TextField(max_length=400)
    answered = BooleanField(default=False)
    alteration = DateTimeField(auto_now=True)

    
class Survey(Model):
    text = TextField(max_length=400)
    option_1 = CharField(max_length=255, blank=True)
    option_2 = CharField(max_length=255, blank=True)
    option_3 = CharField(max_length=255, blank=True)
    option_4 = CharField(max_length=255, blank=True)
    option_5 = CharField(max_length=255, blank=True)
    correct_option = CharField(max_length=255, blank=True)
    finalized = BooleanField(default=False)