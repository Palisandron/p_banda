from django.shortcuts import render
from django.http import HttpResponse
from apps.g_banda.models import Bandolero



# Create your views here.

# Ejemplos de vistas basada en funciones

def index(request):
    # muestra 'index.html'
    return render(request,'index.html')


def Banda(request):
    # muestra 'g_banda/banda.html' en la carpeta 'templates'      
    bando = Bandolero.objects.exclude(activo = 'False').order_by('instrumento')
    contexto = {'bandoleros':bando }
    
    return render(request,'g_banda/banda.html',contexto)

def Usuarios(request):
    # muestra login.html
    return render(request,'g_banda/login.html')    

#================================================================================    