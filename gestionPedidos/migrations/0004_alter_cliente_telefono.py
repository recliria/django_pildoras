# Generated by Django 5.0.7 on 2024-07-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=7, verbose_name='celular'),
        ),
    ]
