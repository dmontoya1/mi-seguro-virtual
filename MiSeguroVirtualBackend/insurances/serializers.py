from rest_framework import serializers


from .models import (
    UserPolicy,
    Insurance, 
    InsuranceRequest, 
    Insurance,
    Metadata,
    MetadataChoices
)

class MetadataChoicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetadataChoices
        fields = ('id', 'value')


class MetadataSerializer(serializers.ModelSerializer):

    related_choices = MetadataChoicesSerializer(many=True, read_only=True)

    class Meta:
        model = Metadata
        fields = ('id', 'name', 'field_type', 'related_choices', 'is_required')


class InsuranceSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Insurance
        fields = ('id', 'category', 'name', 'image')


class InsuranceDetailSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(many=False)
    related_metadata = MetadataSerializer(many=True, read_only=True)

    class Meta:
        model = Insurance
        fields = ('id', 'category', 'name', 'image', 'related_metadata')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceRequest
        fields = ('status', 'request_date', 'client', 'insurance','broker', 'adviser_code')

        def create(self, validated_data):
            request_insurance = InsuranceRequest.objects.create(**validated_data)
            return request_insurance


class RequestGetSerializer(serializers.ModelSerializer):

    insurance = InsuranceSerializer(many=False, read_only=True)

    class Meta:
        model = InsuranceRequest
        fields = ('status', 'request_date', 'client', 'insurance','broker', 'adviser_code')

        def create(self, validated_data):
            request_insurance = InsuranceRequest.objects.create(**validated_data)
            return request_insurance


class UserPolicySerializer(serializers.ModelSerializer):
    
    insurance_request = RequestGetSerializer(many=False, read_only=True)
    insurer = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserPolicy
        fields = ('insurance_request', 'insurer', 'insurance_file', 'adviser_mail', 'expiration_date', 'effective_date')
