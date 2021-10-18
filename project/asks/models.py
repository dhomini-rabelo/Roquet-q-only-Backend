from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, ManyToManyField, IntegerField)


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
    creator = CharField(max_length=128)
    text = TextField(max_length=400)
    answered = BooleanField(default=False)
    creation = DateTimeField(auto_now_add=True)
    up_votes = PositiveIntegerField(default=0)
    down_votes = PositiveIntegerField(default=0)
    score = IntegerField(default=0)
    
    def update_score(self):
        self.score = self.up_votes - self.down_votes
    

    
    