# Generated by Django 3.1.3 on 2021-07-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_auto_20210713_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date_order'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
    ]
