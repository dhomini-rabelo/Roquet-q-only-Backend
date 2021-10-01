from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)


class Theme(Model):
    name = CharField(max_length=128)
    

class Room(Model):
    title = CharField(max_length=128)
    creator = CharField(max_length=128)
    code = PositiveIntegerField()
    themes = TextField(max_length=5)