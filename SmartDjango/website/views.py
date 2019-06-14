from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View

import io
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template

from .models import Cliente, Fornecedor, Servicos
from .forms import FornecedorForm, ClienteForm
from .filters import FornecedorFilter, ClienteFilter
from .utils import render_to_pdf

class FornecedorPdf(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        fornecedor = Fornecedor.objects.all()
        template = get_template('pdf_fornecedor.html')
        context = {
            "fornecedor_nome_fantasia": fornecedor.nome_fantasia,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf_fornecedor.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            return response
        return HttpResponse("Arquivo não encontrado.")

class ClientePdf(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cliente = Cliente.objects.get()
        template = get_template('pdf_cliente.html')
        context = {
            "cliente_nome": cliente.nome,
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf_cliente.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            return response
        return HttpResponse("Arquivo não encontrado.")

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