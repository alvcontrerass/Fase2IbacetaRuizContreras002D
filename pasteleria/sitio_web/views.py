from django.shortcuts import render
from django.http import HttpResponse 
from django.core.mail import send_mail
from django.conf import settings

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

def enviar_formulario(request):

    if request.method=="POST":
        
        nombre   = request.POST["nombre"]
        email    = request.POST["email"]
        telefono = request.POST["telefono"]
        fecha    = request.POST["fecha"]
        comment  = request.POST["comentario"]

        emai_from=settings.EMAIL_HOST_USER
        recipient_list=['momentosdulces.pasteleriaa@gmail.com']

        subject = "Contacto desde formulario WEB"
        message = 'Se ha recibido un contacto desde la página WEB \nNombre: %s Email: %s \nTelefono: %s \nFecha: %s \nComentario: \n %s' % (nombre, email, telefono, fecha, comment)

        send_mail(subject, message, emai_from, recipient_list)
        
        return render (
        request,
        'formulario.html',
        context={}
        )