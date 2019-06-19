from django import forms
from .models import Cliente, Fornecedor, Servico, Produto, Orcamento

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

class OrcamentoForm(forms.ModelForm):
    metro = forms.DecimalField(
        label ='Metro² '
    )

    class Meta:

        model = Orcamento

        fields = {
            'cliente',
            'fornecedor',
            'produto',
            'preco',
            'servico',
            'metro'
        }

class ProdutoForm(forms.ModelForm):
    marca = forms.CharField(
        label='Produto ')
    descricao = forms.CharField(
        label='Descricao',
        widget=forms.Textarea,
        required = False)
    class Meta:

        model = Produto

        fields = [
            'marca',
            'descricao',
            'fornecedor'
        ]

class ServicoForm(forms.ModelForm):
    nome = forms.CharField(
        label='Serviço ',
        widget=forms.TextInput(attrs={'placeholder': 'Nome do Serviço'}))
    descricao = forms.CharField(
        label='Descrição ',
        widget=forms.Textarea,
        required = False)
    
    class Meta:

        model = Servico

        fields = [
            'nome',
            'descricao'
        ]

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome ',
        widget=forms.TextInput(attrs={'placeholder': 'Nome completo do cliente'}))
    cpf = forms.CharField(
        max_length=11,
        label='CPF ',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 111.111.111-11'}))
    email = forms.EmailField(
        label='E-mail ',
        widget=forms.TextInput(attrs={'placeholder': 'seuemail@mail.com'}))
    endereco = forms.CharField(
        label='Endereço ',
        widget=forms.TextInput(attrs={'placeholder': 'Rua/Av Número Bairro'})
    )
    complemento = forms.CharField(
        label='Complemento (Opcional)',
        required = False,
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
        max_length=8,
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
        max_length=13,
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 111111111111'}))
    razao_social = forms.CharField(
        label='Razão Social ',
        widget=forms.TextInput(attrs={'placeholder': 'Padaria Pão de Ló LTDA'}))
    email = forms.EmailField(
        label='E-mail ',
        widget=forms.TextInput(attrs={'placeholder': 'seuemail@mail.com'}))
    endereco = forms.CharField(
        label='Endereço ',
        widget=forms.TextInput(attrs={'placeholder': 'Rua/Av Número Bairro'})
    )
    complemento = forms.CharField(
        label='Complemento (Opcional)',
        required = False,
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
        max_length=8,
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