from django.db import models
from django.utils import timezone

#import datetime

# Create your models here.

class Evento(models.Model):
    tipo = models.CharField('Tipo',max_length=30)
    fecha_evento = models.DateField('Fecha')
    hora = models.TimeField('Hora')
    lugar = models.CharField('Lugar',max_length=50)
    notas = models.TextField(blank = True, null = True)

    class Meta:
        ordering = ["-fecha_evento"]


    def __str__(self):
        return   str(self.fecha_evento) +'---'+self.tipo