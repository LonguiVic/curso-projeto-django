from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Longui'
    })


def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')