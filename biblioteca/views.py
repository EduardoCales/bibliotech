from django.shortcuts import render
from django.views import generic

class LoginView(generic.TemplateView):
    template_name = 'biblioteca/login.html'

class CadastroView(generic.TemplateView):
    template_name = 'biblioteca/cadastro.html'
