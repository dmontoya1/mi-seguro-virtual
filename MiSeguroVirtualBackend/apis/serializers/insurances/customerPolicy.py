from rest_framework import serializers

from insurances.models import CustomerPolicy


class CustomerPolicySerializer(serializers.ModelSerializer):


    customer = serializers.StringRelatedField(many=False)
    insurer = serializers.StringRelatedField(many=False)
    insurance = serializers.StringRelatedField(many=False)


    class Meta:


        model = CustomerPolicy
        fields = ('customer', 'insurer', 'insurance', 'adviser_code', 'adviser_mail', 'expiration_date', 'effective_date', 'licensed_plate')