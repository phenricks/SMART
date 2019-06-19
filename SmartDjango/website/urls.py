from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from .views import IndexTemplateView, \
    create_fornecedor, update_fornecedor, delete_fornecedor, fornecedor_filter, FornecedorPdf, \
    create_cliente, update_cliente, delete_cliente, cliente_filter, ClientePdf, \
    create_servico, update_servico, delete_servico, lista_servico, create_produto, lista_produto, \
    update_produto, delete_produto, create_orcamento, lista_orcamento, OrçamentoPdf, delete_orcamento, \
    update_orcamento

app_name = 'website'

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('home/', IndexTemplateView.as_view(), name="index"),
    
    path('criar/fornecedor/', create_fornecedor, name='criar_fornecedor'),
    path('atualiza/fornecedor/<int:id>/', update_fornecedor, name='atualiza_fornecedor'),
    path('deleta/fornecedor/<int:id>/', delete_fornecedor, name='deleta_fornecedor'),
    path('filtro/fornecedor', fornecedor_filter, name='filtra_fornecedor'),
    path('fornecedor/pdf/<int:id>/', FornecedorPdf.as_view(), name='fornecedor_pdf'),

    path('criar/cliente/', create_cliente, name='criar_cliente'),
    path('atualiza/cliente/<int:id>/', update_cliente, name='atualiza_cliente'),
    path('deleta/cliente/<int:id>/', delete_cliente, name='deleta_cliente'),
    path('filtro/cliente', cliente_filter, name='filtra_cliente'),
    # URL NÃO UTILIZADA, DEIXADA SOMENTE PARA FUTURAS REFERÊNCIAS!
    #path('cliente/pdf/<int:id>/', ClientePdf.as_view(), name='cliente_pdf'),

    path('criar/servico/', create_servico, name='criar_servico'),
    path('atualiza/servico/<int:id>/', update_servico, name='atualiza_servico'),
    path('deleta/servico/<int:id>/', delete_servico, name='deleta_servico'),
    path('lista/servico/', lista_servico, name='lista_servico'),

    path('criar/produto/', create_produto, name='criar_produto'),
    path('atualiza/produto/<int:id>/', update_produto, name='atualiza_produto'),
    path('deleta/produto/<int:id>/', delete_produto, name='deleta_produto'),
    path('lista/produto/', lista_produto, name='lista_produto'),

    path('orcamento/', create_orcamento, name='orcamento'),
    path('lista/orcamento/', lista_orcamento, name='lista_orcamento'),
    path('pdf/<int:id>/', OrçamentoPdf.as_view(), name='pdf'),
    path('deleta/orcamento/<int:id>/', delete_orcamento, name='deleta_orcamento'),
    path('atualiza/orcamento/<int:id>/', update_orcamento, name='atualiza_orcamento')
]