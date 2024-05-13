from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'bibliotech/login.html')

def cadastro(request):
    return render(request, 'bibliotech/cadastro.html')

def home(request):
    return HttpResponse('home')
