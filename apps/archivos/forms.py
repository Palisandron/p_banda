from django import forms
from .models import Archivos
from django.forms import ModelForm


# Para subir un archivo, File_Upload


class Archivo_Form(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ['nombre','tipo','docfile']





