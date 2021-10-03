from django.urls import path
from .views import *

urlpatterns = [
    path('perguntar', ask, name='ask'),
]
