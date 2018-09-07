from rest_framework import serializers

from insurances.models import InsuranceRequest, Insurance
from users.models import Customer


class RequestSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Insurance
        fields = ('state', 'request_date')