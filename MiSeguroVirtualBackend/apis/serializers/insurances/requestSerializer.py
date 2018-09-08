from rest_framework import serializers

from insurances.models import InsuranceRequest, Insurance
from users.models import Customer


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceRequest
        fields = ('state', 'request_date','customer', 'insurance')

        def create(self, validated_data):
            request_insurance = InsuranceRequest.objects.create(**validated_data)
            return request_insurance
