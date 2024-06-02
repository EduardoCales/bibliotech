from django.contrib import admin
from .models import Category, Livro, Autor, Usuario

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)

@admin.register(Autor)
class AutroAdmin(admin.ModelAdmin):
    ...

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'sobrenome', 'email', 'senha', 'covers', 'cpf', 'endereco', 'telefone')