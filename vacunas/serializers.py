from rest_framework import serializers
from .models import Vacuna

class VacunaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacuna
        fields = ['id', 'nombre', 'fabricante', 'tipo', 'cant_dosis']