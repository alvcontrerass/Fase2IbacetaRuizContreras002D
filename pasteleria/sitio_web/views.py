from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def inicio(request):
    return render(
        request,
        'index.html'
    )

def catalogo(request):
    return render(
        request,
        'productos.html'
    )

def contacto(request):
    return render (
        request,
        'formulario.html'
    )