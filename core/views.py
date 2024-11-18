from django.shortcuts import render, redirect, get_object_or_404
from django_filters.views import FilterView
from .models import Cliente, Produto, Venda
from .forms import ClienteForm, ProdutoForm, VendaForm
from .filters import ClienteFilter, ProdutoFilter, VendaFilter


# --- Cliente ---
def cliente_list(request):
    filtro = ClienteFilter(request.GET, queryset=Cliente.objects.all())
    return render(request, 'clientes.html', {'filter': filtro})


def cliente_form(request, id=None):
    cliente = get_object_or_404(Cliente, id=id) if id else None
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})


# --- Produto ---
def produto_list(request):
    filtro = ProdutoFilter(request.GET, queryset=Produto.objects.all())
    return render(request, 'produtos.html', {'filter': filtro})


def produto_form(request, id=None):
    produto = get_object_or_404(Produto, id=id) if id else None
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})


# --- Venda ---
def venda_list(request):
    filtro = VendaFilter(request.GET, queryset=Venda.objects.select_related('cliente', 'produto'))
    return render(request, 'vendas.html', {'filter': filtro})


def venda_form(request, id=None):
    venda = get_object_or_404(Venda, id=id) if id else None
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'venda_form.html', {'form': form})