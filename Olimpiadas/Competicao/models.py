from django.db import models

# Create your models here.

class Competicao(models.Model):
    
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=100)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()


    def __str__(self):
        return self.nome

class Atleta(models.Model):
    
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()
    tempo_chegada_atleta = models.FloatField()
    metros_dardo = models.FloatField()
    
    def __str__(self):
        return self.nome