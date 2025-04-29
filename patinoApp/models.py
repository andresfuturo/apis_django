from django.db import models

class Automovil(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()
    diseño = models.CharField(max_length=100)
    cilindraje = models.IntegerField()

    class Meta:
        verbose_name = "Automóvil"
        verbose_name_plural = "Automóviles"
