# Generated by Django 5.0.7 on 2024-07-23 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articulos',
            new_name='Articulo',
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
    ]
