import django_filters

from .views import Fornecedor, Cliente

class FornecedorFilter (django_filters.FilterSet):
    class Meta:
        model = Fornecedor
        fields = {
            'nome_fantasia',
            'razao_social', 
            'cidade',
            'estado',
        }

class ClienteFilter (django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = {
            'nome',
            'cidade',
            'estado',
        }
