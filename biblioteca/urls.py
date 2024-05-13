from django.urls import path
from biblioteca.views import login, cadastro, home


urlpatterns = [
    path('', login),
    path('cadastro/', cadastro),
    path('home/', home),
]