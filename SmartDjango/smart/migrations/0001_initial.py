# Generated by Django 2.1.5 on 2019-05-11 02:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereço', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=255)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=255)),
                ('endereço', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereço', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
    ]
