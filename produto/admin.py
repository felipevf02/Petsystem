from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'id_produto', 'nm_produto', 'tipo', 'descricao', 'vl_unidade', 'unidade_medida', 'preco_fornecedor',
        'preco_venda', 'estoque', 'created_at', 'created_by', 'updated_at', 'updated_by')
    list_display_links = ('id_produto', 'nm_produto')
    list_per_page = 10
    search_fields = ('id_produto', 'nm_produto', 'tipo')
    list_editable = ('descricao', 'vl_unidade', 'unidade_medida', 'preco_fornecedor', 'preco_venda')


admin.site.register(Produto, ProdutoAdmin)
