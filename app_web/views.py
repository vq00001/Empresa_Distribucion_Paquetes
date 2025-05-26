from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def seguimiento_paquete(request, codigo_paquete):
    return HttpResponse('codigo paquete: %s' % codigo_paquete)