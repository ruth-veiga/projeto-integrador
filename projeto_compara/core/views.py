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

def tela_precos(request, id):
    produto = Produto.objects.get(id=id)
    mercados = Mercado.objects.all()
    mercados_produtos = produtos_mercados.objects.filter(produto = produto)
    precificados = []
    for linha in mercados_produtos:
        precificados.append(linha.mercado)
        linha.preco = float(linha.preco)

    return render(request, 'precos.html', {'produto': produto, 'mercados': mercados, 'mercados_produtos': mercados_produtos, 'precificados': precificados})

def adicionar_precos(request, id):
    mercados = Mercado.objects.all()
    produto = Produto.objects.get(id=id)
    for mercado in mercados:
        preco_mercado = request.POST.get(f'{mercado.id}')
        try:
            existencia = produtos_mercados.objects.get(mercado=mercado, produto=produto)
            existencia.preco = preco_mercado
            existencia.save()
        except:
            if float(preco_mercado) > 0:
                produtos_mercados.objects.create(mercado=mercado, produto=produto, preco=preco_mercado)
    return redirect(lista_produtos)
