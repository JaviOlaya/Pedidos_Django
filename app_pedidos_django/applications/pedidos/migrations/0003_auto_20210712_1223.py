# Generated by Django 3.1.3 on 2021-07-12 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20210712_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_created',
            new_name='user_order',
        ),
    ]