from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cidade)
admin.site.register(Categoria)
admin.site.register(Mercado)
admin.site.register(Produto)
admin.site.register(produtos_mercados)
admin.site.register(Sessão)