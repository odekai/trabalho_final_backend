from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm


def product_list(request):
    produtos = Produto.objects.all()
    return render(request, 'products/product_list.html', {'produtos': produtos})


def product_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect('product_list')
    else:
        form = ProdutoForm()

    return render(request, 'products/product_form.html', {'form': form, 'title': 'Adicionar Produto'})


def product_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado!")
            return redirect('product_list')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'products/product_form.html', {'form': form, 'title': 'Editar Produto'})


def product_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        produto.delete()
        messages.success(request, "Produto deletado!")
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {'produto': produto})
