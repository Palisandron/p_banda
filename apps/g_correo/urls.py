from django.contrib import admin
from django.urls import path

from .views import contactoView, hechoView

urlpatterns = [
    path('contacto/', contactoView, name='contacto'),
    path('hecho/', hechoView, name='hecho'),
]