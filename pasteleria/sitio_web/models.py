from django.db import models

# Create your models here.

class Producto(models.Model):

    codigo_producto=models.AutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=1000)
    valor=models.IntegerField()
    imagen=models.ImageField()

class Pedido_cabecera(models.Model):

    numero_pedido=models.AutoField(primary_key=True)
    fecha_creacion=models.DateField()
    hora_creacion=models.TimeField()
    fecha_entrega=models.DateField()
    hora_entrega=models.TimeField()
    rut_cliente=models.CharField(max_length=10)
    nombre_cliente=models.CharField(max_length=100)
    telefono_cliente=models.IntegerField()
    email_cliente=models.EmailField()
    direccion_entrega=models.CharField(max_length=200)
    valor_total=models.IntegerField()



class Pedido_posicion(models.Model):

    numero_pedido=models.ForeignKey(Pedido_cabecera, on_delete=models.CASCADE)
    codigo_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    valor_posicion=models.IntegerField()
