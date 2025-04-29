from django.contrib import admin
from .models import Automovil

# Clase para personalizar el panel de administración
class AutomovilAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "marca",
        "modelo",
        "diseño",
        "cilindraje",
    )

# Registro del modelo Automovil con configuración personalizada
admin.site.register(Automovil, AutomovilAdmin)
