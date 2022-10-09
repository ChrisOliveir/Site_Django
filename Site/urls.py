# Não é recomendado criar url no arquivo de rotas do projeto!

from django.urls import path

from .views import index, contato

urlpatterns = [
    path('',index),
    path('contato',contato)
]

