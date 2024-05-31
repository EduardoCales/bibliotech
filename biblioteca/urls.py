from django.urls import path
from .views import LoginView, CadastroView


urlpatterns = [
   path('', LoginView.as_view(), name='login'),
   path('cadastro/', CadastroView.as_view(), name='cadastro'),
]