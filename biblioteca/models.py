from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=65)

     def __str__(self):
        return self.name
     
class Autor(models.Model):
    nome = models.CharField(max_length=65)
    nacionalidade = models.CharField(max_length=65)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
     nome = models.CharField(max_length=65)
     sobrenome = models.CharField(max_length=65)
     email = models.CharField(max_length=65)
     senha = models.CharField(max_length=65)
     covers = models.ImageField(upload_to='biblioteca/covers/%Y/%m/%d/')
     cpf = models.CharField(max_length=14)
     endereco = models.CharField(max_length=165)
     telefone = models.CharField(max_length=15)

     def __str__(self):
         return self.nome

class Livro(models.Model):
     title = models.CharField(max_length=65)
     description = models.CharField(max_length=165)
     created_ad = models.DateTimeField(auto_now_add=True)
     is_published = models.BooleanField(default=False)
     covers = models.ImageField(upload_to='biblioteca/covers/%Y/%m/%d/')
     category = models.ForeignKey(
          Category, on_delete=models.SET_NULL, null=True
          )
     autor = models.ForeignKey(
         Autor, on_delete=models.SET_NULL, null=True
     )

     def __str__(self):
         return self.title
