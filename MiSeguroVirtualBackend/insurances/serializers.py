from rest_framework import serializers

from users.models import Customer

from .models import CustomerPolicy, Insurance, InsuranceRequest, Insurance


class CustomerPolicySerializer(serializers.ModelSerializer):


    customer = serializers.StringRelatedField(many=False)
    insurer = serializers.StringRelatedField(many=False)
    insurance = serializers.StringRelatedField(many=False)

    class Meta:
        model = CustomerPolicy
        fields = ('customer', 'insurer', 'insurance', 'adviser_code', 'adviser_mail', 'expiration_date', 'effective_date')


class InsureranceSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Insurance
        fields = ('category','name')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceRequest
        fields = ('state', 'request_date','customer', 'insurance','broker', 'adviser_code')

        def create(self, validated_data):
            request_insurance = InsuranceRequest.objects.create(**validated_data)
            return request_insurance