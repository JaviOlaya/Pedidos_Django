from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.
class Product (TimeStampedModel):
    G_CHOICES = (
        ('HOMBRE', 'HOMBRE'),
        ('MUJER', 'MUJER'),
        ('OTROS', 'OTROS'),
    )

    COLOR_CHOICES = (
        ('ROJO', 'ROJO'),
        ('VERDE', 'VERDE'),
        ('NARANJA','NARANJA'),
        ('AMARILLO', 'AMARILLO'),
        ('BLANCO', 'BLANCO'),
        ('NEGRO', 'NEGRO'),
        ('MARRON', 'MARRON')
    )

    SIZE_CHOICES = (
        ('32','32'),
        ('34','34'),
        ('36','36'),
        ('38','38'),
        ('40','40'),
        ('42','42'),
        ('44','44'),
        ('46','46')
    )

    name = models.CharField('Nombre', max_length=80)
    description = models.TextField('Descripcion producto',max_length=200, blank=True)
    g_model = models.CharField('Género',max_length=30, choices=G_CHOICES)
    color_model = models.CharField('Color',max_length=30, choices=COLOR_CHOICES)
    size_model = models.CharField('Talla',max_length=30, choices=COLOR_CHOICES)
    price = models.DecimalField()('Precio',max_digits=10, decimal_places=2 )
    stock = models.PositiveIntegerField('Stock', default=0),
    num_sales = models.PositiveIntegerField('Unidades vendidas', default=0)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="prod_created",
        )


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id)+ ' ' + str(self.name)
