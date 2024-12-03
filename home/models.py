from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - Quantidade: {self.quantidade} - R${self.valor:.2f}"
