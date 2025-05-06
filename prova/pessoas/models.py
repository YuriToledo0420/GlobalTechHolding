from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    idade = models.IntegerField()
    altura = models.FloatField()
    peso = models.FloatField()

    def __str__(self):
        return self.nome
