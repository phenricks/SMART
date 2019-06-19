import django_filters

from .views import Fornecedor, Cliente

class FornecedorFilter (django_filters.FilterSet):
    nome_fantasia = django_filters.CharFilter(
        label='Nome Fantasia',
        lookup_expr='icontains')
    razao_social = django_filters.CharFilter(
        label='Razão Social',
        lookup_expr='icontains')
    cidade = django_filters.CharFilter(
        label='Cidade',
        lookup_expr='icontains')
    estado = django_filters.CharFilter(
        label='Estado',
        lookup_expr='icontains')
    class Meta:
        model = Fornecedor
        fields = {
            'nome_fantasia',
            'razao_social', 
            'cidade',
            'estado',
        }

class ClienteFilter (django_filters.FilterSet):
    nome = django_filters.CharFilter(
        label='Nome',
        lookup_expr='icontains')
    cidade = django_filters.CharFilter(
        label='Cidade',
        lookup_expr='icontains')
    estado = django_filters.CharFilter(
        label='Estado',
        lookup_expr='icontains')
    dt_criacao = django_filters.CharFilter(
        label='Cliente Desde',
        lookup_expr='icontains')
    class Meta:
        model = Cliente
        fields = {
            'nome',
            'cidade',
            'estado',
            'dt_criacao',
        }