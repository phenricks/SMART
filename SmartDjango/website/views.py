from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View, ListView

from decimal import *
import io
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from .models import Cliente, Fornecedor, Servico, Produto, Orcamento
from .forms import FornecedorForm, ClienteForm, ServicoForm, ProdutoForm, OrcamentoForm
from .filters import FornecedorFilter, ClienteFilter
from .utils import render_to_pdf

# CRUD Orçamento
#------------------------------------------------------------------------------------------------
@login_required
def create_orcamento(request):
    form = OrcamentoForm(request.POST or None)

    if form.is_valid():
        
        form.save()
        return redirect('website:lista_orcamento')

    return render(request, 'gerar_orcamento.html', {'form': form})

@login_required
def lista_orcamento(request):
    orcamento = Orcamento.objects.all()

    return render(request, 'lista_orcamento.html', {'orcamento': orcamento})

@login_required
def delete_orcamento(request, id):
    orcamento = Orcamento.objects.get(id=id)

    if request.method == 'POST':
        orcamento.delete()
        return redirect('website:lista_orcamento')

    return render(request, 'deleta_orcamento.html', {'orcamento': orcamento})

@login_required
def update_orcamento(request, id):
    orcamento = Orcamento.objects.get(id=id)
    form = OrcamentoForm(request.POST or None, instance=orcamento)

    if form.is_valid():
        orcamento.save()
        return redirect('website:lista_orcamento')
    
    return render(request, 'atualiza_orcamento.html', {'form': form, 'orcamento': orcamento})

#------------------------------------------------------------------------------------------------

# CRUD Produtos
#------------------------------------------------------------------------------------------------
@login_required
def create_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('website:filtra_fornecedor')

    return render(request, 'criar_produto.html', {'form': form})

@login_required
def update_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        produto.save()
        return redirect('website:lista_produto')

    return render(request, 'atualiza_produto.html', {'form': form, 'produto': produto})

@login_required
def lista_produto(request):
    produto = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produto': produto})

@login_required
def delete_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('website:lista_produto')

    return render(request, 'deleta_produto.html', {'produto': produto})
#------------------------------------------------------------------------------------------------

# CRUD Serviços
#------------------------------------------------------------------------------------------------
@login_required
def create_servico(request):
    if request.user.is_superuser:
        form = ServicoForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('website:lista_servico')

        return render(request, 'criar_servico.html', {'form': form})
    else:
        return redirect('website:index')

@login_required
def lista_servico(request):
    if request.user.is_superuser:
        servicos = Servico.objects.all()
        return render(request, 'lista_servicos.html', {'servicos': servicos})
    else:
        return redirect('website:index')

@login_required
def update_servico(request, id):
    if request.user.is_superuser:
        servicos = Servico.objects.get(id=id)
        form = ServicoForm(request.POST or None, instance=servicos)

        if form.is_valid():
            servicos.save()
            return redirect('website:lista_servico')
    
        return render(request, 'atualiza_servico.html', {'form': form, 'servicos': servicos})
    else:
        return redirect('website:index')

@login_required
def delete_servico(request, id):
    if request.user.is_superuser:    
        servicos = Servico.objects.get(id=id)

        if request.method == 'POST':
            servicos.delete()
            return redirect('website:lista_servico')

        return render(request, 'deleta_servico.html', {'servicos': servicos})
    else:
        return redirect('website:index')
#------------------------------------------------------------------------------------------------

# PDF
#------------------------------------------------------------------------------------------------
class FornecedorPdf(LoginRequiredMixin, View):
    def get(self, request, id):
        fornecedor = Fornecedor.objects.get(id=id)
        instance = fornecedor
        context = {
            'fornecedor': instance.nome_fantasia,
            'cnpj': instance.cnpj,
            'razao_social': instance.razao_social,
            'email': instance.email,
            'endereco': instance.endereco,
            'complemento': instance.complemento,
            'cidade': instance.cidade,
            'estado': instance.estado,
            'cep': instance.cep,
        }
        pdf = render_to_pdf('pdf_fornecedor.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            return response
        return HttpResponse("Arquivo não encontrado.")

class ClientePdf(LoginRequiredMixin, View):
    def get(self, request, id):
        cliente = Cliente.objects.get(id=id)
        instance = cliente
        context = {
            'cliente': instance.nome,
            'cpf': instance.cpf,
            'email': instance.email,
            'endereco': instance.endereco,
            'complemento': instance.complemento,
            'cidade': instance.cidade,
            'estado': instance.estado,
            'cep': instance.cep,
            'desde': instance.dt_criacao,
            'soma': instance.cep + instance.cpf
        }
        pdf = render_to_pdf('pdf_cliente.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            return response
        return HttpResponse("Arquivo não encontrado.")

class OrçamentoPdf(LoginRequiredMixin, View):
    def get(self, request, id):
        orcamento = Orcamento.objects.get(id=id)
        preco = str(orcamento.preco)
        p = Decimal(preco)
        pre = round(p,1)
        m = Decimal(orcamento.metro)
        met = round(m,1)
        
        context = {
            'cliente': orcamento.cliente,
            'servico': orcamento.servico,
            'metro': orcamento.metro,
            'preco': orcamento.preco,
            'desde': orcamento.dt_criacao,
            'fornecedor': orcamento.fornecedor,
            'total': pre * met
        }
        pdf = render_to_pdf('pdf_orcamento.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            return response
        return HttpResponse("Arquivo não encontrado.")
#------------------------------------------------------------------------------------------------

# HomePage
#------------------------------------------------------------------------------------------------
class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
#------------------------------------------------------------------------------------------------

# CRUD Fornecedor
# -----------------------------------------------------------------------------------------------

@login_required
def create_fornecedor(request):
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('website:filtra_fornecedor')

    return render(request, 'criar_fornecedor.html', {'form': form})

@login_required
def update_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        fornecedor.save()
        return redirect('website:filtra_fornecedor')
    
    return render(request, 'atualiza_fornecedor.html', {'form': form, 'fornecedor': fornecedor})

@login_required
def delete_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('website:filtra_fornecedor')

    return render(request, 'deleta_fornecedor.html', {'fornecedor': fornecedor})

@login_required
def fornecedor_filter(request):
    lista_fornecedor = Fornecedor.objects.all()
    filtro_fornecedor = FornecedorFilter(request.GET, queryset=lista_fornecedor)
    return render(request, 'filtro_fornecedor.html', {'filter': filtro_fornecedor})
#------------------------------------------------------------------------------------------------

# CRUD Cliente
# -----------------------------------------------------------------------------------------------

@login_required
def create_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('website:filtra_cliente')

    return render(request, 'criar_cliente.html', {'form': form})

@login_required
def update_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        cliente.save()
        return redirect('website:filtra_cliente')
    
    return render(request, 'atualiza_cliente.html', {'form': form, 'cliente': cliente})

@login_required
def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('website:filtra_cliente')

    return render(request, 'deleta_cliente.html', {'cliente': cliente})

@login_required
def cliente_filter(request):
    lista_cliente = Cliente.objects.all()
    filtro_cliente = ClienteFilter(request.GET, queryset=lista_cliente)
    return render(request, 'filtro_cliente.html', {'filter': filtro_cliente})
#------------------------------------------------------------------------------------------------