from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase, punctuation
from random import choices


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    length = int(request.GET.get('length', 10))
    characters = ascii_lowercase
    if request.GET.get('uppercase'):
        characters += ascii_uppercase
    if request.GET.get('numbers'):
        characters += '0123456789'
    if request.GET.get('special'):
        characters += punctuation
    thepassword = ''.join(choices(characters, k=length))
    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')