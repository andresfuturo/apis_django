from rest_framework.routers import DefaultRouter
from ventasApp.api.views import VentaViewSet

router_venta = DefaultRouter()
router_venta.register(r'ventas', VentaViewSet, basename='ventas')
