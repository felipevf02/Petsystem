from django.db import models
from django.utils import timezone


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
