from website.views import IndexTemplateView, ClienteListView, ClienteUpdateView, ClienteCreateView, \
    ClienteDeleteView, FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('home/', IndexTemplateView.as_view(), name="index"),

    # GET /cliente/cadastrar
    path('cliente/cadastrar', ClienteCreateView.as_view(), name="cadastra_cliente"),

    # GET /clientes
    path('clientes/', ClienteListView.as_view(), name="lista_clientes"),

    # GET/POST /cliente/{pk}
    path('cliente/<pk>', ClienteUpdateView.as_view(), name="atualiza_cliente"),

    # GET/POST /cliente/excluir/{pk}
    path('cliente/excluir/<pk>', ClienteDeleteView.as_view(), name="deleta_cliente"),

    # GET /fornecedor/cadastrar
    path('fornecedor/cadastrar', FornecedorCreateView.as_view(), name="cadastra_fornecedor"),

    # GET /fornecedores
    path('fornecedores/', FornecedorListView.as_view(), name="lista_fornecedores"),

    # GET/POST /fornecedor/{pk}
    path('fornecedor/<pk>', FornecedorUpdateView.as_view(), name="atualiza_fornecedores"),

    # GET/POST /fornecedor/excluir/{pk}
    path('fornecedor/excluir/<pk>', FornecedorDeleteView.as_view(), name="deleta_fornecedor"),
]
