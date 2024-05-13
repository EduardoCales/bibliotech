from django.contrib import admin
from .models import Category, Livro

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
