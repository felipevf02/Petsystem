from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Produto
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    produtos = Produto.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(produtos, 5)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request, 'produto/index.html', {
        'produtos': produtos
    })


def ver_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if not produto.mostrar:
        raise Http404()

    return render(request, 'produto/ver_produto.html', {
        'produto': produto
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404

    campos = Concat('nome', Value(' '), 'sobrenome')

    produtos = Produto.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))

    # print(produtos.query)
    paginator = Paginator(produtos, 5)

    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request, 'produtos/index.html', {
        'produtos': produtos
    })