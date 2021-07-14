from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel


#Traer el modelo de los productos
from applications.productos.models import Product
from applications.usuarios.models import User

#Traer el serializador de pedidos
from .managers import OrderDetailManager
# Create your models here.

class Order(TimeStampedModel):
    STATE_CHOICES = (
        ('0','Seleccionar'),
        ('1','En proceso'),
        ('2','Enviado'),
        ('3','Entregado')    
    )

    PAYMENT_CHOICES =(
        ('0','SELECCIONAR'),
        ('1','TARJETA'),
        ('2','METALICO'),
        ('3','CONTRAREEMBOLSO')
    )

    date_order = models.DateTimeField('Fecha de pedido', blank = True,null = True)
    count = models.PositiveIntegerField('Cantidad de Productos')
    amount = models.DecimalField('Importe del pedido', max_digits=10, decimal_places=2)
    content = RichTextField('Notas', max_length=300, blank=True)
    address_send = models.TextField('Direccion de envio', blank = True) 
    order_state = models.CharField('Estado del pedido: ',max_length=30, choices=STATE_CHOICES,default ='0')
    payment_state = models.CharField('Estado del pago: ',max_length=30, choices=PAYMENT_CHOICES,default='0')
    close = models.BooleanField('Pedido cerrado', default=False)
    anulate = models.BooleanField(default=False)
    user_order = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="usuario_pedido",
    )

    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Nº de pedido'+str(self.id) + ' - ' + 'Fecha : '+str(self.date_order)

class OrderDetail(TimeStampedModel):
    
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        verbose_name='Codigo de Pedido'
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    count =models.PositiveIntegerField('Cantidad')

    price_order = models.DecimalField('Precio Pedido', max_digits=10, decimal_places=2)
    anulate = models.BooleanField(default=False)
    objects = OrderDetailManager()

    class Meta:
        verbose_name = 'Detalle pedido'
        verbose_name_plural = 'Detalles de un pedido'

    