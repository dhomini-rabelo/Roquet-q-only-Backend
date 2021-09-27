from django.shortcuts import render

BP = 'apps/core' # base path

def home(request):
    return render(request,f'{BP}/home.html')