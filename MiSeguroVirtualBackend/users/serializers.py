
from django.contrib.auth import authenticate, user_logged_in
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

from users.models import User, TermsAcceptanceLogs


class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        print("Validation")
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        print (credentials)

        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)
            print (user)
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


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'document_id', 'user_type')


class InfluencerSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'code', 'document_type', 'document_id', 'email', 'phone_number' )


class InfluencerBankSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = User
        fields = ('pk', 'bank', 'account_type', 'account_number')


class ChangePasswordSerializer(serializers.ModelSerializer):
	"""Serializador para cambiar el password de un usuario
	"""

	class Meta:
		model = User
		fields = ('password',)

	def save(self):
		change_password = self.context['request'].data.get('password',None)
		if change_password != None:
			user = User.objects.get(
				email=self.context['request'].data['email']
			)
			if self.context['request'].data['old_password'] == change_password:
				raise serializers.ValidationError("La contraseña nueva es igual a la anterior, por favor verifica tu información")
			check = check_password(self.context['request'].data['old_password'], user.password)
			if check == True:
				user.set_password(self.context['request'].data['password'])
				user.save()
			else:
				raise serializers.ValidationError("La contraseña ingresada no corresponde a la de tu cuenta")
			return user
		super(ChangePasswordSerializer, self).save()
