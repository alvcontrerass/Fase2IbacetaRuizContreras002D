from django.test import TestCase
from . models import Producto, Pedido_posicion
#comentario arreglo nombre git

class PastelesTestCase(TestCase):
    def setup(self):
        a1=Producto.objects.create(codigo_producto=5)
        a2=Producto.objects.create(codigo_producto=2)
        Pedido_posicion.objects.create(codigo_produto=a1, cantidad=1)
        Pedido_posicion.objects.create(codigo_produto=a2, cantidad=2)

    def test_pastel_pedido(self):
        pedido1 = Pedido_posicion.objects.get(cantidad=1)
        self.assertEqual(pedido1.Producto.codigo_producto, 5)