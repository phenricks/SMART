from django import forms

from smart.models import Cliente
from smart.models import Fornecedor


# FORMULÁRIO DE INCLUSÃO DE CLIENTES
# -------------------------------------------

class InsereClienteForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email@docliente.com'}),required = True)
    cpf = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Ex.: 111.111.111-11'}),required = True)
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),required = True)
    endereço = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Rua Número Bairro Cidade Estado País'}),required = True)

    class Meta:
        model = Cliente

        fields = [
            'nome',
            'endereço',
            'cpf', 
	    'email'
        ]

# FORMULÁRIO DE INCLUSÃO DE FORNECEDORES
# -------------------------------------------
class InsereFornecedorForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Fornecedor

        # Campos que estarão no form
        fields = [
            'razao_social',
            'endereço',
            'cnpj',
	    'nome_fantasia',
	    'email'
        ]
