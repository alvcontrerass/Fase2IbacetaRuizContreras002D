from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class User(models.Model):
    nom=models.CharField(max_length=50)
    ape=models.CharField(max_length=50)
    cumple=models.DateField
    dire=models.CharField(max_length=150)
    contra=models.CharField(max_length=30)

class Formulario(models.Model):
    nomfor=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    fono=models.CharField(max_length=12)
    fechapedido=models.DateField
    motivo="aqui que va xd? radiobutton"
    comentario=models.TextField

class Pasteles(models.Model):
	nompas = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	precio = models.DateField

	cantidadpersonas = (
		('12', '12 Personas'),
		('16', '16 Personas'),
		('18', '18 Personas'),
		('24', '24 Personas'),
        ('30', '30 Personas'),
        ('36', '36 Personas'),
        ('45', '45 Personas'),
	)

	status = models.CharField(
		max_length=2,
		choices=cantidadpersonas,
		blank=True,
		default='12',
		help_text='Cantidad de personas',
	)

