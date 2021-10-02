from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('criar-sala', create_room, name='create_room'),
    path('entrar-na-sala', enter_room, name='enter_room'),
]
