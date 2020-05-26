from django import forms

class ContactoForm(forms.Form):
    Tu_correo = forms.EmailField(required=True)
    asunto = forms.CharField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)