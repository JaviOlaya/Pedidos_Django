from django.db import models

class ProductManager(models.Manager):
    def producto_usuario(self,usuario):
        return self.filter(
            user_created = usuario,
            
        )
    #Creamos una función que nos muestre productos si hay stock
    def productos_stock(self):

        return self.filter(
            stock__gt=0,

        ).order_by('num_sales')