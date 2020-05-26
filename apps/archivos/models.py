from django.db import models
from django.forms import ModelForm
import os

# Create your models here.
class Archivos(models.Model):
    docfile = models.FileField()
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Archivos"
    
    
    def __str__(self):
        return self.nombre

    def lista():
        path = 'static/media'
        listado = os.listdir(path)
        return listado

    def delete(self,*args,**kwargs):
        self.docfile.delete()
        super().delete(*args,**kwargs)