from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def usuario(request, id):
    return HttpResponse('id usuario: %s' % id)

def estadisticas(request): # eficiencia de rutas
    return HttpResponse('Implementar con BDD')

def asignacion_de_rutas(request):
    return HttpResponse('Implementar con modulo de rutas')

def seguimiento_paquete(request, codigo_paquete):
    return HttpResponse('codigo paquete: %s' % codigo_paquete)