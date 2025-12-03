from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm


def client_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clients/client_list.html', {'clientes': clientes})


def client_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado!")
            return redirect('client_list')
    else:
        form = ClienteForm()

    return render(request, 'clients/client_form.html', {'form': form, 'title': 'Novo Cliente'})


def client_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado!")
            return redirect('client_list')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clients/client_form.html', {'form': form, 'title': 'Editar Cliente'})


def client_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, "Cliente removido!")
        return redirect('client_list')

    return render(request, 'clients/client_confirm_delete.html', {'cliente': cliente})
