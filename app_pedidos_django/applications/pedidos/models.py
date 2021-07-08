from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Order(TimeStampedModel):

    count = models.PositiveIntegerField('Cantidad de Productos')
    amount = models.DecimalField('Importe pedido', max_digits=10, decimal_places=2)
    close = models.BooleanField('Pedido cerrado', default=False)
    anulate = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Usuario Pedido",
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

    count =models.PositiveIntegerField('Cantidad')

    price_order = models.DecimalField(
        'Precio Pedido', 
        max_digits=10, 
        decimal_places=2
    )
    anulate = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Detalle pedido'
        verbose_name_plural = 'Detalles de un pedido'