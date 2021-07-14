# Generated by Django 3.1.3 on 2021-07-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20210712_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='address_send',
        ),
        migrations.AddField(
            model_name='order',
            name='address_send',
            field=models.TextField(blank=True, verbose_name='Direccion de envio'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_state',
            field=models.CharField(choices=[('0', 'Seleccionar'), ('1', 'En proceso'), ('2', 'Enviado'), ('3', 'Entregado')], default='0', max_length=30, verbose_name='Estado del pedido: '),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_state',
            field=models.CharField(choices=[('0', 'SELECCIONAR'), ('1', 'TARJETA'), ('2', 'METALICO'), ('3', 'CONTRAREEMBOLSO')], default='0', max_length=30, verbose_name='Estado del pedido: '),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe del pedido'),
        ),
    ]