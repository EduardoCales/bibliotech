from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
     name = models.CharField(max_length=65)

     def __str__(self):
        return self.name

class Livro(models.Model):
     title = models.CharField(max_length=65)
     description = models.CharField(max_length=165)
     created_ad = models.DateTimeField(auto_now_add=True)
     is_published = models.BooleanField(default=False)
     covers = models.ImageField(upload_to='biblioteca/covers/%Y/%m/%d/')
     category = models.ForeignKey(
          Category, on_delete=models.SET_NULL, null=True
          )
     author = models.ForeignKey(        
          User, on_delete=models.SET_NULL, null=True
          )
     
     def __str__(self):
         return self.title
     '''
     Tem q criar a tabela usuario e criar a tabela de autor.
     A tabela de autor deve ser uma chave primaria de Livro, pois 
     um livro tem um autor.
     '''
     
     '''
     class Autor(models.Model):
     nome = models.ChairField(max_lenght=65)
     nacionalidade = models.ChairField(max_lenght)
     '''

     """
     class Usuario(models.Model):
     nome = models.CharField(max_lenght=65)
     sobrenome = models.CharField(max_lenght=65)
     email = models.ChairField(max_lenght=65)
     foto = models.ImageField(upload_to='biblioteca/covers/%Y/%m/%d/')
     cpf = models.ChairField()
     endereco = models.ChairField()
     telefone()
     """

     '''
     class Emprestimo(models.Model):
     data_retirada = models.DateTimeField(auto_now_add=True)
     previsao_devolucao = models.DateTimeField(auto_now_add=True)
     data_devolucao = models.DateTimeField(auto_now_add=True)
     
     '''
