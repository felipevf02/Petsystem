from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Produto
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    produtos = Produto.objects.order_by('id_produto')
    paginator = Paginator(produtos, 5)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request, 'produto/index.html', {
        'produtos': produtos
    })


def form_user(request):
    return render(request, 'cadastros/form_users.html', {
})
def form_product(request):
    return render(request, 'cadastros/form_product.html', {
})
def form_forn(request):
    return render(request, 'cadastros/form_forn.html', {
})
def form_entrada(request):
    return render(request, 'cadastros/form_entrada.html', {
})
def form_saida(request):
    return render(request, 'cadastros/form_saida.html', {
})

def table_user(request):
    return render(request, 'consultas/table_users.html', {
})
def table_product(request):
    return render(request, 'consultas/table_product.html', {
})
def table_forn(request):
    return render(request, 'consultas/table_forn.html', {
})
def table_entrada(request):
    return render(request, 'consultas/table_entrada.html', {
})
def table_saida(request):
    return render(request, 'consultas/table_saida.html', {
})

def signin(request):
    return render(request, 'signin.html', {
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

