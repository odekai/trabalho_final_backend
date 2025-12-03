
from django.contrib.auth.models import AbstractUser
from django.db import models

class Funcionario(AbstractUser):
    TIPOS = (
        ("ADM", "Administrador"),
        ("FUNC", "Funcionário"),
    )

    tipo = models.CharField(max_length=4, choices=TIPOS, default="FUNC")

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"
