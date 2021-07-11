from django.db import models
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel
from django.conf import settings
# Create your models here.
class Product (TimeStampedModel):
    #MARCAS CONSTANTES
    M1 = '0'
    M2 = '1'
    M3 = '2'
    M4 = '3'
    M5 = '4'
    M6 = '5'
    B_CHOICES =[
        (M1, 'MARCA1'),
        (M2, 'MARCA2'),
        (M3, 'MARCA3'),
        (M4, 'MARCA4'),
        (M5, 'MARCA5'),
        (M6, 'MARCA6'),
    ]

    #GENERO CONSTANTES
    HOMBRE = '0'
    MUJER = '1'
    OTROS = '2'
    G_CHOICES = [
        (HOMBRE, 'HOMBRE'),
        (MUJER, 'MUJER'),
        (OTROS, 'OTROS'),
    ]

    #CONSTANTES COLORES
    ROJO ='1'
    VERDE ='2'
    NARANJA ='3'
    AMARILLO ='4'
    BLANCO ='5'
    NEGRO = '6'
    MARRON = '7'

    COLOR_CHOICES = [
        (ROJO, 'ROJO'),
        (VERDE, 'VERDE'),
        (NARANJA,'NARANJA'),
        (AMARILLO, 'AMARILLO'),
        (BLANCO, 'BLANCO'),
        (NEGRO, 'NEGRO'),
        (MARRON, 'MARRON')
    ]
#CONSTANTES DE TALLA
    S1='0'
    S2='1'
    S3='2'
    S4='3'
    S5='4'
    S6='5'
    S7='6'
    S8='7'
    SIZE_CHOICES = [
        (S1,'32'),
        (S2,'34'),
        (S3,'36'),
        (S4,'38'),
        (S5,'40'),
        (S6,'42'),
        (S7,'44'),
        (S8,'46')
    ]
    date_order = models.DateTimeField('Tipo de Venta',)
    product_name = models.CharField('Nombre', max_length=80)
    brand = models.CharField('Marca',max_length=30, choices=B_CHOICES)
    description = RichTextField('Descripcion producto',max_length=300, blank=True)
    g_model = models.CharField('Genero',max_length=30, choices=G_CHOICES)
    color_model = models.CharField('Color',max_length=30, choices=COLOR_CHOICES)
    size_model = models.CharField('Talla',max_length=30, choices=SIZE_CHOICES)
    price = models.DecimalField('Precio',max_digits=10, decimal_places=2 )
    stock = models.PositiveIntegerField('Stock', default=0),
    num_sales = models.PositiveIntegerField('Unidades vendidas', default=0)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="prod_created",
        )


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id)+ ' ' + str(self.product_name)
