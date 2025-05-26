from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage),
    path('seguimiento/<int:codigo_paquete>', views.seguimiento_paquete)
] 