
from rest_framework import serializers

from .models import Benefits


class BenefitsSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Benefits
        fields = '__all__'
