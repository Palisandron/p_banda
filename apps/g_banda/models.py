from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Bandolero(models.Model):
    # por omisión se crea un campo id autoincremental
    nombre = models.CharField(max_length=30)
    apellidos =  models.CharField(max_length=50)
    instrumento =  models.CharField(max_length=30)
    # estos campos no son obligatorios, admiten blancos y null
    direccion =  models.CharField(max_length=150,blank = True, null = True)
    telefono =  models.CharField(max_length=12,blank = True, null = True)
    email =  models.EmailField(blank = True, null = True)
    fecha_alta = models.DateField(blank = True, null = True)
    fecha_baja = models.DateField(blank = True, null = True)
    tipo =  models.CharField(max_length=20,blank = True, null = True)
    activo =  models.BooleanField(default=True)
    notas = models.TextField(blank = True, null = True)
    edad = models.IntegerField(blank = True, null = True,default=0)
    
    def __str__(self):
	    return self.nombre +' '+self.apellidos +'----- '+self.instrumento