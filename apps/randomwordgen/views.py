from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
    'random_word': get_random_string(length=14) 
    
    }
    print "fuckingdjango"
    return render(request, 'randomwordgen/index.html', context)

