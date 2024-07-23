from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7,verbose_name="celular")

class Articulo(models.Model):

    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):

        return "El artículo {}, pertenece a la sección {}, con un precio de {}".format(self.nombre,self.seccion,self.precio)

class Pedido(models.Model):

    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()