from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Venda, ItemVenda
from .forms import VendaForm, ItemVendaForm


@login_required
def sale_list(request):
    vendas = Venda.objects.all()
    return render(request, 'sales/sale_list.html', {'vendas': vendas})


@login_required
def sale_create(request):
    if not request.user.funcionario.tipo == 'FUNCIONARIO':
        messages.error(request, "Somente funcionários podem registrar vendas.")
        return redirect('sale_list')

    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.funcionario = request.user.funcionario
            venda.save()
            messages.success(request, "Venda iniciada!")
            return redirect('sale_add_item', venda.id)
    else:
        form = VendaForm()

    return render(request, 'sales/sale_form.html', {'form': form})


@login_required
def sale_add_item(request, venda_id):
    venda = Venda.objects.get(id=venda_id)

    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.venda = venda
            item.save()

            venda.valor_total += item.produto.preco * item.quantidade
            venda.save()

            messages.success(request, "Item adicionado!")
            return redirect('sale_add_item', venda.id)
    else:
        form = ItemVendaForm()

    itens = ItemVenda.objects.filter(venda=venda)

    return render(request, 'sales/sale_items.html', {
        'venda': venda,
        'form': form,
        'itens': itens,
    })
