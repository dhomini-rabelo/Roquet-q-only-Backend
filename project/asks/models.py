from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, ManyToManyField)


class Option(Model):
    text = CharField(max_length=255)
    votes = PositiveIntegerField(blank=True)
    correct = BooleanField(default=False)


class Survey(Model):
    creator = CharField(max_length=128, default='')
    text = TextField(max_length=400)
    options = ManyToManyField(Option, blank=True)
    finalized = BooleanField(default=False)
    creation = DateTimeField(auto_now_add=True, blank=True)


class Question(Model):
    creator = CharField(max_length=128, default='')
    text = TextField(max_length=400)
    answered = BooleanField(default=False)
    creation = DateTimeField(auto_now_add=True, blank=True)
    up_votes = PositiveIntegerField(blank=True)
    down_votes = PositiveIntegerField(blank=True)
    

    
    