from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from apps.g_eventos.models import Evento


# Create your views here.

def Galeria(request):
    # muestra 'g_eventos/galeria.html' en la carpeta 'templates'  
    return render(request,'g_eventos/galeria.html')


# Ejemplo de vista basada en clases
class Lista_Eventos(ListView):
    model = Evento
    template_name = 'g_eventos/eventos.html'


    
