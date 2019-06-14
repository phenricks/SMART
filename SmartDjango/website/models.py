from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.IntegerField(null=False, blank=False, unique=True)
    email = models.CharField(max_length=255, null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    estado = models.CharField(max_length=60, null=False, blank=False)
    cep = models.IntegerField(null=False, blank=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return self.nome_fantasia

class Servicos(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, unique=True)
    descricao = models.CharField(max_length=1000, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    marca = models.CharField(max_length=60, null=False, blank=False)
    descricao = models.CharField(max_length=1000, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.marca