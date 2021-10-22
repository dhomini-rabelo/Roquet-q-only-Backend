from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, CASCADE)
from django.db.models.fields.related import ManyToManyField

    
    
    
class Room(Model):
    creator = CharField(max_length=128, default='')
    code = PositiveIntegerField(unique=True)
    password_admin = CharField(max_length=128)

    def __str__(self):
        return f'Room {self.code}'



class Theme(Model):
    creator = CharField(max_length=128, default='')
    name = CharField(max_length=128)
    active = BooleanField(default=True)
    room = ForeignKey(Room, on_delete=CASCADE, related_name='themes', null=True)
    
    def __str__(self):
        return self.name
