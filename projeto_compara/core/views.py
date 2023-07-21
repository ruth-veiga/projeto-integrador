from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos, 'categorias':categorias})

def cadastrar_produtos(request):
    nome_produto = request.POST.get('nome')
    produto_descricao = request.POST.get('descricao')
    id_categoria = request.POST.get('categoria')

    produto_categoria = Categoria.objects.get(id=id_categoria)

    Produto.objects.create(nome= nome_produto, descricao=produto_descricao, categoria=produto_categoria)
    return redirect(lista_produtos)

def lista_mercados(request):
    mercados = Mercado.objects.all()
    cidades = Cidade.objects.all()
    # rua = Mercado.object.all()
    # cidade = Mercado.objects.all()
    return render(request, 'mercados.html', {'mercados': mercados, 'cidades': cidades})

def cadastrar_mercados(request):
    nome_mercado = request.POST.get('nome')
    rua_mercado = request.POST.get('rua')
    bairro_mercado = request.POST.get('bairro')
    numero_mercado = request.POST.get('numero')

    id_cidade = request.POST.get('cidade')

    cidade_mercado = Cidade.objects.get(id=id_cidade)
     
    Mercado.objects.create(nome=nome_mercado, rua=rua_mercado, cidade=cidade_mercado, bairro=bairro_mercado,numero=numero_mercado)
    return redirect(lista_mercados)
