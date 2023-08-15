from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
    
class Sessão(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=60)
    sessao = models.ForeignKey(Sessão, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Mercado(models.Model):
    nome = models.CharField(max_length=60)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=40)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to ='imagens_mercados/')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=60, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to ='imagens_produtos/')

    def __str__(self):
        if self.imagem == '':
            return 'Sem imagem'
        return self.nome

class produtos_mercados(models.Model):
    mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.produto.nome} | {self.mercado.nome} | {self.preco} "