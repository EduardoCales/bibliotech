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
     author = models.ForeignKey(        #<-- Esse cara aqui tem q trocar pq ta como usuario
          User, on_delete=models.SET_NULL, null=True
          )
     
     def __str__(self):
         return self.title
     
     #Precisa criar uma tabela de author com nome