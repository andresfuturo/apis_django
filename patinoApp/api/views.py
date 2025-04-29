from rest_framework.viewsets import ModelViewSet
from patinoApp.models import Automovil
from patinoApp.api.serializers import AutomovilSerializer

class AutomovilViewSet(ModelViewSet):
    queryset = Automovil.objects.all()
    serializer_class = AutomovilSerializer
