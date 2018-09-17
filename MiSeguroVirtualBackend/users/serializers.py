
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

from users.models import User, TermsAcceptanceLogs


class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)
                user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class TermsAcceptanceLogsSerializer(serializers.ModelSerializer):
    """customer = CustomerSerializer(many=False)"""

    class Meta:
        model = TermsAcceptanceLogs
        fields = ('ip_address', 'Acceptance_date', 'customer')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = User
        fields = ('cellphone_number', 'document_number', 'user')
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_primary_data = dict(username = user_data['username'], password = user_data['password'])
        user = User.objects.create_user(**user_primary_data)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.email = user_data['email']
        user.save()
        customer = Customer.objects.create(user = user, **validated_data)
        return customer