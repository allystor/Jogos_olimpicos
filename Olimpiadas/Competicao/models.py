from django.db import models

# Create your models here.

class Competicao(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()
    
    def __str__(self):
        return self.nome