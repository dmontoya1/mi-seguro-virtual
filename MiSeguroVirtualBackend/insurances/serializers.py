from rest_framework import serializers


from .models import UserPolicy, Insurance, InsuranceRequest, Insurance


class UserPolicySerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    insurer = serializers.StringRelatedField(many=False)
    insurance = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserPolicy
        fields = ('customer', 'insurer', 'insurance', 'adviser_code', 'adviser_mail', 'expiration_date', 'effective_date')


class InsureranceSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Insurance
        fields = ('category','name')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceRequest
        fields = ('state', 'request_date', 'user', 'insurance','broker', 'adviser_code')

        def create(self, validated_data):
            request_insurance = InsuranceRequest.objects.create(**validated_data)
            return request_insurance