from rest_framework import viewsets
from ventasApp.models import Venta
from ventasApp.api.serializers import VentaSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
