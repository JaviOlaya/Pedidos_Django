from django.db import models
from django.db.models import Q,Count, Avg, Sum

from applications.productos.models import Product
#from .models import OrderDetail ,Order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    .models import OrderDetail

class OrderManager(models.Manager):

    def products_by_order(self, order_id):
        consulta = self.filter(
            o_id = order_id
        ).order_by('count', 'product_name')
        return consulta
    def precio_total_pedido(self, order_id):
        resultado =self.annotate(
             sum_importes=sum('price')
        )
        return resultado

class OrderDetailManager(models.Manager):
    def num_de_productos_por_pedido(sef, order_id):
        consulta = Count('product')
        return consulta