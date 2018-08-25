from rest_framework import serializers

from users.models import Customer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','email','password','cellphone_number','document_number')