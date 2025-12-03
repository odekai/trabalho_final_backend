from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fidelidade = models.BooleanField(default=False)
    pontos = models.IntegerField(default=0)

    def adicionar_pontos(self, valor_compra):
        self.pontos += int(valor_compra // 10)
        self.save()

    def __str__(self):
        return self.nome
