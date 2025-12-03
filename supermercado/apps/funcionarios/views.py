from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Funcionario
from .forms import FuncionarioForm, LoginForm


def employee_list(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/lista.html', {'funcionarios': funcionarios})


def employee_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário cadastrado!")
            return redirect('employee_list')
    else:
        form = FuncionarioForm()

    return render(request, 'funcionarios/form.html', {'form': form, 'titulo': 'Novo Funcionário'})


def employee_update(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário atualizado!")
            return redirect('employee_list')
    else:
        form = FuncionarioForm(instance=funcionario)

    return render(request, 'funcionarios/form.html', {'form': form, 'titulo': 'Editar Funcionário'})


def employee_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)

    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, "Funcionário removido!")
        return redirect('employee_list')

    return render(request, 'funcionarios/delete.html', {'funcionario': funcionario})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            user = authenticate(username=usuario, password=senha)
            
            if user:
                login(request, user)
                messages.success(request, "Login efetuado!")
                return redirect('employee_list')
            else:
                messages.error(request, "Credenciais incorretas.")
    else:
        form = LoginForm()

    return render(request, 'funcionarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da conta.")
    return redirect('login')
