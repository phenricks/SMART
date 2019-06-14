from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from .views import create_fornecedor, update_fornecedor, delete_fornecedor, \
    create_cliente, update_cliente, delete_cliente, IndexTemplateView, \
    fornecedor_filter, cliente_filter, ClientePdf, FornecedorPdf

app_name = 'website'

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('home/', IndexTemplateView.as_view(), name="index"),
    
    path('criar/fornecedor/', create_fornecedor, name='criar_fornecedor'),
    path('filtro/fornecedor', fornecedor_filter, name='filtra_fornecedor'),
    path('atualiza/fornecedor/<int:id>/', update_fornecedor, name='atualiza_fornecedor'),
    path('deleta/fornecedor/<int:id>/', delete_fornecedor, name='deleta_fornecedor'),
    path('fornecedor/pdf/<int:id>/', FornecedorPdf.as_view(), name='fornecedor_pdf'),

    path('filtro/cliente', cliente_filter, name='filtra_cliente'),
    path('criar/cliente/', create_cliente, name='criar_cliente'),
    path('atualiza/cliente/<int:id>/', update_cliente, name='atualiza_cliente'),
    path('deleta/cliente/<int:id>/', delete_cliente, name='deleta_cliente'),
    path('cliente/pdf/<pk>/', ClientePdf.as_view(), name='cliente_pdf'),
]