from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, ManyToManyField, IntegerField)



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
    

    
    