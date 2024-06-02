from django.urls import path
from . import views


urlpatterns = [
   path('', views.login, name='login'),
   path('cadastro/', views.cadastro, name='cadastro'),
   path('validar_login/', views.validar_login, name='validar_login'),
   path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
   path('home/', views.home, name='home')
]