from rest_framework import serializers

from insurances.models import Insurance


class InsureranceSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Insurance
        fields = ('category','name')