from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from smart.models import Cliente
from smart.models import Fornecedor
from website.forms import InsereFornecedorForm
from website.forms import InsereClienteForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE CLIENTES
# ----------------------------------------------

class ClienteListView(ListView):
    template_name = "website/lista_clientes.html"
    model = Cliente
    context_object_name = "clientes"


# CADASTRAMENTO DE CLIENTES
# ----------------------------------------------

class ClienteCreateView(CreateView):
    template_name = "website/cria_cliente.html"
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy("website:lista_clientes")


# ATUALIZAÇÃO DE CLIENTES
# ----------------------------------------------

class ClienteUpdateView(UpdateView):
    template_name = "website/atualiza_clientes.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("website:lista_clientes")


# EXCLUSÃO DE CLIENTES
# ----------------------------------------------

class ClienteDeleteView(DeleteView):
    template_name = "website/exclui_clientes.html"
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy("website:lista_clientes")

# LISTA DE FORNECEDORES
# ----------------------------------------------

class FornecedorListView(ListView):
    template_name = "website/lista_fornecedores.html"
    model = Fornecedor
    context_object_name = "fornecedores"

# CADASTRAMENTO DE FORNECEDORES
# ----------------------------------------------

class FornecedorCreateView(CreateView):
    template_name = "website/cria_fornecedor.html"
    model = Fornecedor
    form_class = InsereFornecedorForm
    success_url = reverse_lazy("website:lista_fornecedores")

# ATUALIZAÇÃO DE CLIENTES
# ----------------------------------------------

class FornecedorUpdateView(UpdateView):
    template_name = "website/atualiza_fornecedores.html"
    model = Fornecedor
    fields = '__all__'
    context_object_name = 'fornecedor'
    success_url = reverse_lazy("website:lista_fornecedores")

# EXCLUSÃO DE FORNECEDORES
# ----------------------------------------------

class FornecedorDeleteView(DeleteView):
    template_name = "website/exclui_fornecedores.html"
    model = Fornecedor
    context_object_name = 'fornecedor'
    success_url = reverse_lazy("website:lista_fornecedores")
