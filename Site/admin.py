from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente # o ponto significa que esta na mesma pasta que o arquivo admin

admin.site.register(Produto)
admin.site.register(Cliente)
