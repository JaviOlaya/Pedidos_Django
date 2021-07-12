from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel


#Traer el modelo de los productos
from applications.productos.models import Product


#Traer el serializador de pedidos
from .managers import OrderDetailManager
# Create your models here.

class Order(TimeStampedModel):
    date_order = models.DateTimeField('Fecha de pedido', blank = True,null = True)
    count = models.PositiveIntegerField('Cantidad de Productos')
    amount = models.DecimalField('Importe pedido', max_digits=10, decimal_places=2)
    content = RichTextField('Notas', max_length=300, blank=True)
    close = models.BooleanField('Pedido cerrado', default=False)
    anulate = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Comprador',
        related_name="user_order",
        #editable=False
    )

    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    

class OrderDetail(TimeStampedModel):
    
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        verbose_name='Codigo de Pedido'
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address_send = models.TextField('Direccion de envio', blank = True) 
    count =models.PositiveIntegerField('Cantidad')

    price_order = models.DecimalField('Precio Pedido', max_digits=10, decimal_places=2)
    anulate = models.BooleanField(default=False)
    objects = OrderDetailManager()

    class Meta:
        verbose_name = 'Detalle pedido'
        verbose_name_plural = 'Detalles de un pedido'

    def __str__(self):
        return str(self.order.id) + ' - ' + str(self.product.product_name)