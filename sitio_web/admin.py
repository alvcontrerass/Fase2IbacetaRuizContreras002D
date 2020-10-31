from django.contrib import admin

# Register your models here.
from . models import Producto , Pedido_cabecera , Pedido_posicion

admin.site.register(Producto)
admin.site.register(Pedido_cabecera)
admin.site.register(Pedido_posicion)
