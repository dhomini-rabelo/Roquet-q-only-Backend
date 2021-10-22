from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, ManyToManyField, IntegerField, CASCADE)
from room.models import Theme


class Question(Model):
    creator = CharField(max_length=128)
    text = TextField(max_length=512)
    answered = BooleanField(default=False)
    creation = DateTimeField(auto_now_add=True)
    up_votes = PositiveIntegerField(default=0)
    down_votes = PositiveIntegerField(default=0)
    theme = ForeignKey(Theme, on_delete=CASCADE, related_name='questions', null=True)
    

    
    