from django.db import models
from django.db.models import Q,Count, Avg, Sum 

from applications.productos.models import Product

class OrderManager(models.Manager):

    def products_by_order(self, order_id):
        consultation = self.filter(
            o_id = order_id
        ).order_by('count', 'product_name')
        return consultation
    def precio_total_pedido(self, order_id):
        resultado =self.annotate(
             sum_importes=S
             um('price')
        )