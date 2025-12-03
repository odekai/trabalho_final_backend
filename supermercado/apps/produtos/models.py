from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=10)

    def estoque_baixo(self):
        return self.quantidade < self.estoque_minimo

    def __str__(self):
        return self.nome 
