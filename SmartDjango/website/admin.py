from django.contrib import admin
from .models import Fornecedor, Servicos, Produtos

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Servicos)
admin.site.register(Produtos)