from django.db import models
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel
from django.conf import settings
from .managers import ProductManager
# Create your models here.
class Product (TimeStampedModel):
   
    B_CHOICES =(
        ('0', 'MARCA1'),
        ('1', 'MARCA2'),
        ('2', 'MARCA3'),
        ('3', 'MARCA4'),
        ('4', 'MARCA5'),
        ('5', 'MARCA6'),
    )

    G_CHOICES = (
        ('0', 'HOMBRE'),
        ('1', 'MUJER'),
        ('2', 'OTROS'),
    )

    COLOR_CHOICES = (
        ('0', 'ROJO'),
        ('1', 'VERDE'),
        ('2','NARANJA'),
        ('3', 'AMARILLO'),
        ('4', 'BLANCO'),
        ('5', 'NEGRO'),
        ('6', 'MARRON'),
    )

    SIZE_CHOICES = (
        ('0','32'),
        ('1','34'),
        ('2','36'),
        ('3','38'),
        ('4','40'),
        ('5','42'),
        ('6','44'),
        ('7','46'),
    )

    product_name = models.CharField('Nombre', max_length=80, blank = False,unique=True, null = False)
    brand = models.CharField('Marca',max_length=30, choices = B_CHOICES,)
    description = RichTextField('Descripcion producto',max_length = 300, blank = False, null = False)
    g_model = models.CharField('Genero',max_length=30, choices=G_CHOICES)
    color_model = models.CharField('Color',max_length=30, choices = COLOR_CHOICES)
    size_model = models.CharField('Talla',max_length=30, choices = SIZE_CHOICES)
    price = models.DecimalField('Precio',max_digits=10, decimal_places=2 )
    stock = models.IntegerField('Stock', default=0)
    num_sales = models.IntegerField('Unidades vendidas', default=0)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="prod_created",
    )


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id)+ ' ' + str(self.product_name)
