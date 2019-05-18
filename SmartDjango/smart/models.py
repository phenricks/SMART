from django.db import models

class Funcionario(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    endereço = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

class Fornecedor(models.Model):

    razao_social = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    endereço = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cnpj = models.CharField(
        max_length=18,
        null=False,
        blank=False
    )

    nome_fantasia = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

class Cliente(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    endereço = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos = models.Manager()
