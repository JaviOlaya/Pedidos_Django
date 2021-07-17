from django.db import models
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel
from django.conf import settings
from .managers import ProductManager


# Create your models here.
class Product (TimeStampedModel):
   
    B1 = '0'
    B2 = '1'
    B3 = '2'
    B4 = '3'
    B5 = '4'
    B6 = '5'
    B7 = '6'

    B_CHOICES =(
        ( B1,'SELECCIONAR...'),
        ( B2, 'MARCA1'),
        ( B3, 'MARCA2'),
        ( B4, 'MARCA3'),
        ( B5, 'MARCA4'),
        ( B6, 'MARCA5'),
        ( B7, 'MARCA6'),
    )

    G1 = '0'
    G2 = '1'
    G3 = '2'
    G4 = '3'
    G_CHOICES = (
        (G1,'SELECCIONAR...'),
        (G2, 'HOMBRE'),
        (G3, 'MUJER'),
        (G4, 'OTROS'),
    )

    C1 ='0'
    C2 ='1'
    C3 ='2'
    C4 ='3'
    C5 ='4'
    C6 ='5'
    C7 ='6'
    C8 ='7'

    COLOR_CHOICES = (
        (C1,'SELECCIONAR...'),
        (C2, 'ROJO'),
        (C3, 'VERDE'),
        (C4,'NARANJA'),
        (C5, 'AMARILLO'),
        (C6, 'BLANCO'),
        (C7, 'NEGRO'),
        (C8, 'MARRON'),
    )

    S1='0'
    S2='1'
    S3='2'
    S4='3'
    S5='4'
    S6='5'
    S7='6'
    S8='7'
    S9='8'
    SIZE_CHOICES = (
        (S1,'SELECCIONAR...'),
        (S2,'32'),
        (S3,'34'),
        (S4,'36'),
        (S5,'38'),
        (S6,'40'),
        (S7,'42'),
        (S8,'44'),
        (S9,'46'),
    )

    product_name = models.CharField('Nombre', max_length=80, blank = False,unique=True, null = False)
    brand = models.CharField('Marca',max_length=30, choices = B_CHOICES)
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

    objects = ProductManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['product_name']
        db_table = 'Product'

    def __str__(self):
        return str(self.id)+ ' ' + str(self.product_name)
