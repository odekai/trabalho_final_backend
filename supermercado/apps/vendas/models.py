from django.db import models
from apps.clientes.models import Cliente
from apps.funcionarios.models import Funcionario
from apps.produtos.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda #{self.id} - {self.data}"


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        # Verificar estoque
        if self.produto.quantidade < self.quantidade:
            raise Exception("Estoque insuficiente.")

        # Baixar do estoque
        self.produto.quantidade -= self.quantidade
        self.produto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
