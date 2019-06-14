from django import forms
from .models import Cliente, Fornecedor

ESTADOS = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome ',
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo do cliente'}))
    cpf = forms.CharField(
        label='CPF ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 111.111.111-11'}))
    email = forms.CharField(
        label='E-mail ',
        widget=forms.TextInput(attrs={'placeholder': 'seuemail@mail.com'}))
    endereco = forms.CharField(
        label='Endereço ',
        widget=forms.TextInput(attrs={'placeholder': 'Rua/Av Número Bairro'})
    )
    complemento = forms.CharField(
        label='Complemento',
        widget=forms.TextInput(attrs={'placeholder': 'Apartamento, Bloco'})
    )
    cidade = forms.CharField(
        label='Cidade ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Belo Horizonte'})
    )
    estado = forms.ChoiceField(
        label='Estado ',
        choices=ESTADOS)
    cep = forms.CharField(
        label='CEP ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 11.111-111'}))

    class Meta:
        
        model = Cliente

        fields = [
            'nome',
            'cpf',
	        'email',
            'endereco',
            'complemento',
            'cidade',
            'estado',
            'cep'
        ]

class FornecedorForm(forms.ModelForm):
    nome_fantasia = forms.CharField(
        label='Nome Fantasia ',
        widget=forms.TextInput(attrs={'placeholder': 'Padaria Smart'}))
    cnpj = forms.CharField(
        label='CNPJ ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 11.1111.1111/11'}))
    razao_social = forms.CharField(
        label='Razão Social ',
        widget=forms.TextInput(attrs={'placeholder': 'Padaria Pão de Ló LTDA'}))
    email = forms.CharField(
        label='E-mail ',
        widget=forms.TextInput(attrs={'placeholder': 'seuemail@mail.com'}))
    endereco = forms.CharField(
        label='Endereço ',
        widget=forms.TextInput(attrs={'placeholder': 'Rua/Av Número Bairro'})
    )
    complemento = forms.CharField(
        label='Complemento ',
        widget=forms.TextInput(attrs={'placeholder': 'Apartamento, Bloco'})
    )
    cidade = forms.CharField(
        label='Cidade ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Belo Horizonte'})
    )
    estado = forms.ChoiceField(
        label='Estado ', choices=ESTADOS)
    cep = forms.CharField(
        label='CEP ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 11.111-111'}))
    

    class Meta:
        
        model = Fornecedor

        fields = [
            'nome_fantasia',
            'cnpj',
            'razao_social', 
	        'email',
            'endereco',
            'complemento',
            'cidade',
            'estado',
            'cep'
        ]