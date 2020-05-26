from django.contrib import admin

#importamos los modelos de la propia app (de ahí el punto)
from .models import Bandolero

# Register your models here.
admin.site.register(Bandolero)