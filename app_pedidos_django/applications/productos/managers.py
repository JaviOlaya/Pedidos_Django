from django.db import models

class ProductManager(models.Manager):
    def producto_por_usuario(self,usuario):
        return self.filter(
            user_created = usuario,
            
        )