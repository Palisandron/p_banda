from django.urls import path,include
from . import views
from apps.g_eventos.views import Lista_Eventos,Galeria


urlpatterns = [
               path('',Lista_Eventos.as_view(),name ='eventos'),
               path('galeria/',views.Galeria,name='galeria'),               
]
