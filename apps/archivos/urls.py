from django.urls import path,include
from . import views
from apps.archivos.views import Lista_archivos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.doc_list, name='archivos'),
    path('borrar/<int:pk>/',views.borrar_archivo,name='borrar'),
    path('subir/',views.upload,name='subir')
     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
