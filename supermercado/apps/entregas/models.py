from django.db import models
from ..produtos.models import Produto


class Entrega(models.Model):
    data = models.DateField()
    nota_fiscal = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Entrega {self.nota_fiscal} - {self.data}"


class ItemEntrega(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        # Atualiza estoque automaticamente ao cadastrar item
        self.produto.quantidade += self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
