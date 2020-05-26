from django.contrib import admin


#importamos los modelos de la propia app (de ahí el punto)
from .models import Evento

# Register your models here.(en el panel de administración)
admin.site.register(Evento)


