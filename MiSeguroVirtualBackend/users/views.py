
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.utils import timezone

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken

from users.models import User, TermsAcceptanceLogs

from .serializers import CustomerSerializer, JWTSerializer, InfluencerSerializer, ChangePasswordSerializer,\
                         InfluencerBankSerializer


class CustomerViewSet(APIView):
    serializer_class = CustomerSerializer
    permission_classes = ()

    def post(self, request, format=None):
        ip_user = get_client_ip(request)
        user_data = dict(
            username=request.data['username'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            password=request.data['password'],
            document_number=request.data['document_number'],
            cellphone_number=request.data['cellphone_number'],
        )

        serializer = CustomerSerializer(data=user_data)

        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                TermsAcceptanceLogs.objects.create(user=user, ip_address=ip_user)
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:
            print (e)
            print ("Exception")
            return Response(dict(status='error', details=str(e)), status=400)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer


class InfluencerUpdate(generics.UpdateAPIView):
    """ Api para actualizar los datos básicos del influencer
    """

    serializer_class = InfluencerSerializer
    queryset = get_user_model().objects.all()


class InfluencerBankUpdate(generics.UpdateAPIView):
    """ Api para actualizar los datos bancarios del influencer
    """

    serializer_class = InfluencerBankSerializer
    queryset = get_user_model().objects.all()


class UserChangeEmail(generics.UpdateAPIView):
    """Api para actualizar el email de un usuario
    """

    serializer_class = InfluencerSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        email = self.request.data.get('old_email')
        user = get_user_model().objects.get(email=email)
        try:
            obj = get_user_model().objects.get(pk=user.pk)
        except:
            raise ValidationError('No existe un usuario con ese correo')
        return obj


class UserChangePassword(generics.UpdateAPIView):
    """Api para actualizar el email de un usuario
    """

    serializer_class = ChangePasswordSerializer
    queryset = get_user_model().objects.all()


    def get_object(self):
        email = self.request.data.get('email')
        user = User.objects.get(email=email)
        return user