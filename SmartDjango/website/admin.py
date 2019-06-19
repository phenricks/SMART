from django.contrib import admin
from .models import Fornecedor, Cliente, Servico, Produto, Preco

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Servico)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Preco)
admin.site.site_header = 'Administração SMART'
admin.site.site_title = 'Administração SMART'