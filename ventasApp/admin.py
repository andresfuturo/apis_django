from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'automovil', 'fecha_venta', 'precio_final')
    list_filter = ('fecha_venta',)
    search_fields = ('cliente__nombre', 'automovil__nombre')
