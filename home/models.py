from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    email_02 = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)
    senha_02 =  models.CharField(max_length=20)
    criaçao = models.DateTimeField(default=timezone.now)

