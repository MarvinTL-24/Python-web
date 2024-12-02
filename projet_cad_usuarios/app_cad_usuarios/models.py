from django.db import models
from django.contrib.auth.models import User

class Enquete(models.Model):
    pergunta = models.CharField(max_length=255)

class Alternativa(models.Model):
    enquete = models.ForeignKey(Enquete, related_name='alternativas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)

class Resposta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
