from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Funcionario


class FuncionarioForm(UserCreationForm):
    class Meta:
        model = Funcionario
        fields = ['username', 'email', 'password1', 'password2', 'tipo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuário",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
