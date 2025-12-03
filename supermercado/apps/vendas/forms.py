from django import forms
from .models import Venda, ItemVenda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
