from django.db import models
from clienteApp.models import Cliente
from patinoApp.models import Automovil

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    automovil = models.ForeignKey(Automovil, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"{self.cliente.nombre} compró {self.automovil.nombre} por {self.precio_final}"
