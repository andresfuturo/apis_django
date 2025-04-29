from rest_framework.routers import DefaultRouter
from patinoApp.api.views import AutomovilViewSet


router_automovil = DefaultRouter()
router_automovil.register(prefix='automoviles', basename='automovil', viewset=AutomovilViewSet)

