from rest_framework import serializers
from patinoApp.models import Automovil

class AutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovil
        fields = [
            "id",
            "nombre",
            "marca",
            "modelo",
            "diseño",
            "cilindraje",
        ]
