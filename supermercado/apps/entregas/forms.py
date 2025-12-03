from django import forms
from .models import Entrega, ItemEntrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['data', 'nota_fiscal', 'valor_total']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nota_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ItemEntregaForm(forms.ModelForm):
    class Meta:
        model = ItemEntrega
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
