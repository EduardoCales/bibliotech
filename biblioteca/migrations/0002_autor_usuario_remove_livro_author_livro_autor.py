# Generated by Django 5.0.6 on 2024-06-02 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=65)),
                ('nacionalidade', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=65)),
                ('sobrenome', models.CharField(max_length=65)),
                ('email', models.CharField(max_length=65)),
                ('senha', models.CharField(max_length=65)),
                ('covers', models.ImageField(upload_to='biblioteca/covers/%Y/%m/%d/')),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=165)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='livro',
            name='author',
        ),
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.autor'),
        ),
    ]
