from django.db import models
from django.utils import timezone
import datetime


# class Categoria(models.Model):
#     nome = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.nome


class Produto(models.Model):
    id_produto = models.PositiveIntegerField(primary_key=True)
    nm_produto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    vl_unidade = models.DecimalField(max_digits=10, decimal_places=1)
    unidade_medida = models.CharField(max_length=255, blank=True)
    preco_fornecedor = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.DecimalField(max_digits=10, decimal_places=1)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True)
    # foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d')

    def __str__(self):
        # trás o nome do valor ao invés do nome do objeto
        return self.nm_produto


class Fornecedores(models.Model):
    id_fornecedor = models.PositiveIntegerField(primary_key=True)
    nm_fornecedor = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    fl_ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nm_fornecedor


class Entradas(models.Model):
    id_entrada = models.PositiveIntegerField(primary_key=True)
    id_fornecedor = models.ForeignKey(Fornecedores, related_name='id_fornecedor', on_delete=models.DO_NOTHING)
    id_produto = models.ForeignKey(Produto, related_name='id_produto', on_delete=models.DO_NOTHING)
    qtd_produto = models.DecimalField(max_digits=10, decimal_places=2)
    dt_entrada = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True)


class Saida(models.Model):
    id_saida = models.PositiveIntegerField(primary_key=True)
    id_produto = models.ForeignKey(Produto, related_name='id_produto', on_delete=models.DO_NOTHING)
    id_usuario = models.ForeignKey(Produto, related_name='id_usuario', on_delete=models.DO_NOTHING)
    qtd_produto = models.DecimalField(max_digits=10, decimal_places=2)
    dt_saida = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True)


class Usuario(models.Model):
    id_usuario = models.PositiveIntegerField(primary_key=True)
    nm_usuario = models.CharField(max_length=30)
    funcao = models.CharField(max_length=30)
    fl_ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nm_usuario