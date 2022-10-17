from django.shortcuts import render

def index(request):
    context = {
        'Site': ' Vendas de Produtos Gamer'
    }
    return render(request, 'index.html',context)

def contato(request):
    return render(request, 'contato.html')
