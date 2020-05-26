from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import ContactoForm

# Create your views here.

def contactoView(request):
    if request.method == 'GET':
        form = ContactoForm()
    else:
        form = ContactoForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['asunto']
            from_email = form.cleaned_data['Tu_correo']
            message = form.cleaned_data['mensaje']
            try:
                send_mail(subject, message,'bandaemmva@gmail.com', [from_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('hecho')
    return render(request, "g_correo/contacto.html", {'form': form})




def hechoView(request):
    return render(request, "g_correo/hecho.html", {})