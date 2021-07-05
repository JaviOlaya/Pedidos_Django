from model_utils.models import TimeStampedModel

from django.db import models

# Create your models here.
class Usuario(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)
    surname = models.CharField('Apellidos', max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField('Telefono', max_length=15)

    class Meta:

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name + ' ' + self.surname

  
