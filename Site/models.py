#PARA CRIAR MIGRATIONS python manage.py makemigrations e depois python manage.py migrations

from distutils.command.upload import upload
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models


# modelo de dados que é uma classe em python 


class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    descricao = models.CharField('Descrição',max_length=1000)
    preco = models.DecimalField('Preco',decimal_places=2,max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    thumb = models.ImageField(upload_to='thumb_filmes')
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome',max_length=100)
    sobrenome = models.CharField('sobrenome',max_length=100)
    email = models.EmailField('email',max_length=100)

   

