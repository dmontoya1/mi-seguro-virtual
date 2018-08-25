from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Customer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ('cellphone_number', 'document_number', 'user')
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer