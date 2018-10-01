from rest_framework import serializers


from .models import UserPolicy, Insurance, InsuranceRequest, Insurance


class InsureranceSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Insurance
        fields = ('category','name')


class RequestSerializer(serializers.ModelSerializer):

    # client = serializers.StringRelatedField(many=False)
    insurance = InsureranceSerializer(many=False, read_only=True)

    class Meta:
        model = InsuranceRequest
        fields = ('status', 'request_date', 'client', 'insurance','broker', 'adviser_code')

        def create(self, validated_data):
            request_insurance = InsuranceRequest.objects.create(**validated_data)
            return request_insurance


class UserPolicySerializer(serializers.ModelSerializer):
    
    insurance_request = RequestSerializer(many=False, read_only=True)
    insurer = serializers.StringRelatedField(many=False)

    
    class Meta:
        model = UserPolicy
        fields = ('insurance_request', 'insurer', 'insurance_file', 'adviser_mail', 'expiration_date', 'effective_date')
