from django.urls import path,include
from . import views
from apps.g_banda.views import Banda,index,Usuarios

urlpatterns = [
    path('', views.index, name='index'),
    path('banda/',views.Banda,name='bandoleros'),
   
]

