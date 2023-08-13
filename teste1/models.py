from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.BigIntegerField(null = True)
    data_nasc = models.DateField(null = True)