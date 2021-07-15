from django.db import models
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel
from django.conf import settings
from .managers import ProductManager
# Create your models here.
class Product (TimeStampedModel):
   
    B_CHOICES =(
        ('0','SELECCIONAR...'),
        ('1', 'MARCA1'),
        ('2', 'MARCA2'),
        ('3', 'MARCA3'),
        ('4', 'MARCA4'),
        ('5', 'MARCA5'),
        ('6', 'MARCA6'),
    )

    G_CHOICES = (
        ('0','SELECCIONAR...'),
        ('1', 'HOMBRE'),
        ('2', 'MUJER'),
        ('3', 'OTROS'),
    )

    COLOR_CHOICES = (
        ('0','SELECCIONAR...'),
        ('1', 'ROJO'),
        ('2', 'VERDE'),
        ('3','NARANJA'),
        ('4', 'AMARILLO'),
        ('5', 'BLANCO'),
        ('6', 'NEGRO'),
        ('7', 'MARRON'),
    )

    SIZE_CHOICES = (
        ('0','SELECCIONAR...'),
        ('1','32'),
        ('2','34'),
        ('3','36'),
        ('4','38'),
        ('5','40'),
        ('6','42'),
        ('7','44'),
        ('8','46'),
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
        ordering = ['product_name']
        db_table = 'Product'

    def __str__(self):
        return str(self.id)+ ' ' + str(self.product_name)
