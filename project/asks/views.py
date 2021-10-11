from django.shortcuts import render, HttpResponse



BP = 'apps/asks' # base path




def ask(request, code):
    return render(request, f'{BP}/ask.html')