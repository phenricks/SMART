from django.db import models

class Preco(models.Model):
    preco = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        ordering =('preco',)
        verbose_name_plural = 'preços'

    def __str__(self):
        return str(self.preco)

class Cliente(models.Model):

    nome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.IntegerField(verbose_name='pf' , null=False, blank=False, unique=True)
    email = models.CharField(max_length=255, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    estado = models.CharField(max_length=60, null=False, blank=False)
    cep = models.IntegerField(null=False, blank=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255, null=False, blank=False, unique=True)
    nome_fantasia = models.CharField(max_length=255, null=False, blank=False)
    cnpj = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=255, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    estado = models.CharField(max_length=60, null=False, blank=False)
    cep = models.IntegerField(null=False, blank=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome_fantasia',)
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.nome_fantasia

class Servico(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, unique=True)
    descricao = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'serviços'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    marca = models.CharField(max_length=60, null=False, blank=False)
    descricao = models.CharField(max_length=1000, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('marca',)
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.marca

class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, related_name='produto')
    preco = models.ForeignKey(Preco, on_delete=models.SET_NULL, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    metro = models.DecimalField(max_digits=9, decimal_places=2)
    dt_criacao = models.DateTimeField(auto_now_add=True)