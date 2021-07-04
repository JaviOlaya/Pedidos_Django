from model_utils.models import TimeStampedModel

from django.db import models

# Create your models here.
class Cliente(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)
    surname = models.CharField('Apellidos', max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField('Telefono', max_length=15)

    class Meta:

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name + ' ' + self.surname

  
