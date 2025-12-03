from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entrega
from apps.produtos.models import Produto
from .forms import EntregaForm


def delivery_list(request):
    entregas = Entrega.objects.all()
    return render(request, 'deliveries/delivery_list.html', {'entregas': entregas})


def delivery_create(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            entrega = form.save()

            # Atualizar estoque
            for item in entrega.itens.all():
                produto = item.produto
                produto.quantidade += item.quantidade
                produto.save()

            messages.success(request, "Entrega registrada e estoque atualizado!")
            return redirect('delivery_list')
    else:
        form = EntregaForm()

    return render(request, 'deliveries/delivery_form.html', {'form': form})
