# nuevaApp/serializers.py

from rest_framework import serializers
from clienteApp.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'direccion']
