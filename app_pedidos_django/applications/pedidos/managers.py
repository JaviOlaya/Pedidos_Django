from django.db import models

class OrderDetailManager(models.Manager):

    def products_by_order(self, order_id):
        consultation = self.filter(
            o_id = order_id
        ).order_by('count', 'product_name')
        return consultation