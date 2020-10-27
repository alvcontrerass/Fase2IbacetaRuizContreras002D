from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def inicio(request):
    return HttpResponse('maldita shit')

def catalogo(request):
    return HttpResponse('catalogo')

def contacto(request):
    return HttpResponse('contacto')