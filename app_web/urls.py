from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login/', views.login),
    path('seguimiento/<int:codigo_paquete>/', views.seguimiento_paquete),
    path('usuario<int:id>/', views.usuario),
    path('usuario<int:id>/estadisticas', views.estadisticas),
    path('usuario<int:id>/asignacion de rutas', views.asignacion_de_rutas)
]   