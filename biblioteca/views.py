from hashlib import sha256
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario

def login(request):
    status = request.GET.get('status')
    return render(request, 'biblioteca/login.html', {'status': status})
        
def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'biblioteca/cadastro.html', {'status': status})

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email, senha=senha)

    if len(usuario) == 0:
        return redirect('/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/home')


def validar_cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    covers = request.POST.get('covers')
    cpf = request.POST.get('cpf')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')

    usuario = Usuario.objects.filter(email = email)
    
    if len(nome.strip()) == 0 or len(sobrenome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(covers.strip()) == 0 or len(cpf.strip()) == 0 or len(endereco.strip()) == 0 or len(telefone.strip()) == 0:
        # A função strip() é utilizada para remover espaçõs em branco
        return redirect('/cadastro/?status=1')
    
    if len(senha) < 8:
        return redirect('/cadastro/?status=2')
    
    if len(usuario) > 0:
        return redirect('/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, sobrenome = sobrenome, email = email, senha = senha, covers = covers, cpf = cpf, endereco = endereco, telefone = telefone)
        usuario.save()

        return redirect('/cadastro/?status=0')
    except:
        return redirect('/cadastro/?status=4')
    
def home(request):
    return render(request, 'biblioteca/home.html')