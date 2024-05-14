from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'bibliotech/pages/login.html')

def cadastro(request):
    return render(request, 'bibliotech/pages/cadastro.html')

