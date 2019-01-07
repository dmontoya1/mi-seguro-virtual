from rest_framework import serializers
from .models import Police


class PoliceSerializer(serializers.ModelSerializer):
    """
    Serializador para las politicas de la plataforma
    """

    class Meta:
        model = Police
        fields = ('id', 'name', 'police_type', 'text')



