from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'GET':
        return render(request, 'biblioteca/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            return HttpResponse('entrou!') #<-- Aqui deve vir o template da home
        else:
            return HttpResponse('nome ou senha invalidos')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'biblioteca/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Ja existe algume com esse nome') #<-- Um template com uma tela falando isso
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado')# <-- deve mandar para a pagina de login e uma mensagem