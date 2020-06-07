
from django.shortcuts import render,redirect
from django.forms import ModelForm
from django import forms
from .models import Archivos
from .forms import Archivo_Form  # para subir Upload
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import os




def Lista_archivos(request):
    # muestra los archivos de 'static/media' en 'archivos/archivos.html'
    # de momento sin uso
    path = 'static/media'
    lista_archivos = os.listdir(path)
    contexto = {'listado':lista_archivos}
    return render(request,'archivos/archivos.html',contexto)



FILE_TYPES = ['png', 'jpg', 'jpeg','mp3','pdf','mp4']


@login_required
def borrar_archivo(request,pk):
    # pk primary key Archivos
    if request.method == 'POST':
        file = Archivos.objects.get(pk=pk)      
        file.delete()
    return redirect ('archivos')    


def doc_list(request):
    # muestra la lista de archivos disponibles en el servidor
    files = Archivos.objects.all()
    return render(request,'archivos/doc_list.html',{'files':files})


@login_required
def upload(request):
    # segunda versión de subir archivos
    if request.method == 'POST':
        form = Archivo_Form(request.POST,request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.docfile = request.FILES['docfile']
            file_type = user_pr.docfile.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPES:
                return render(request, 'archivos/error.html')
            form.save()
            return redirect('archivos')
    else:
        form = Archivo_Form()        

    return render(request,'archivos/upload.html',{'form':form})    
