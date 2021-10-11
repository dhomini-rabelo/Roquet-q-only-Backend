from django.shortcuts import render, HttpResponse



BP = 'apps/asks' # base path




def ask(request, code):
    return render(request, f'{BP}/ask.html')



def vote(request, code):
    return render(request, f'{BP}/vote.html')



def records_view(request, code):
    return render(request, f'{BP}/records.html')