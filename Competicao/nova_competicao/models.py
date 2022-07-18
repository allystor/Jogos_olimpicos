from django.db import models
import datetime

class Competicao(models.Model):
    
    LOCAL_CHOICES = (
        ('1', 'Arena Corinthians'),
        ('2','Maracanã'),
    )    

    local_da_competicao = models.CharField(max_length=100, choices=LOCAL_CHOICES)
    data= models.DateField(default=datetime.date.today)
    hora = models.TimeField(default=datetime.time(hour=0, minute=0, second=0))
    nome_do_atleta = models.CharField(max_length=100)
    idade_do_atleta = models.IntegerField()
    peso_do_atleta = models.FloatField()
    altura_do_atleta = models.FloatField()
    tempo_de_chegada_na_primeira_prova = models.FloatField(default=None)
    metros_de_distancia = models.IntegerField(default=None)
    
    def __str__(self):
        return self.nome_do_atleta