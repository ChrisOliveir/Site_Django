# Não é recomendado criar url no arquivo de rotas do projeto!
'''
Quando criar as paginas do site sempre tem que criar 3 coisas (url, views, template)

'''

from django.urls import path, include 

from .views import index, contato

urlpatterns = [
    path('',index),
    path('contato',contato)
]

