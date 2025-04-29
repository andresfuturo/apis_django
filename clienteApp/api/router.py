from rest_framework.routers import DefaultRouter
from clienteApp.api.views import ClienteViewSet

router_cliente = DefaultRouter()
router_cliente.register(r'clientes', ClienteViewSet, basename='cliente')
