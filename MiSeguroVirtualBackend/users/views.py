
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.views.generic.base import TemplateView, View

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken

from core.views import send_email
from users.models import User, TermsAcceptanceLogs

from .serializers import CustomerSerializer, JWTSerializer, InfluencerSerializer, ChangePasswordSerializer,\
                         InfluencerBankSerializer


class CustomerDetail(generics.RetrieveUpdateAPIView):
    """Api para ver y actualizar la info de un cliente
    """

    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    model = User

    def get_object(self):
        return self.request.user


class CustomerViewSet(APIView):
    serializer_class = CustomerSerializer
    permission_classes = ()

    def post(self, request, format=None):
        ip_user = get_client_ip(request)
        email = request.data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            return Response({'error': 'El correo ya se encuentra registrado, por favor inicia sesión'},
                             status=status.HTTP_400_BAD_REQUEST)
        password = make_password(request.data['password'])

        user_data = dict(
            username=request.data['username'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            password=password,
            document_id=request.data['document_id'],
            phone_number=request.data['phone_number'],
            user_type = User.CLIENTE,
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
            return Response({'error': 'Ha ocurrido un error inesperado. Intenta nuevamente en unos minutos'}, status=status.HTTP_400_BAD_REQUEST)


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


class PasswordCreateView(TemplateView):
    """
    Clase para la creación de la contraseña de un usuario registrado por el SuperAdmin
    """
    template_name = "users/password_set.html"

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token', None)
        if token is not None:
            try:
                user = User.objects.get(token=token)
                return render(
                    request,
                    'users/password_set.html',
                    {
                        'token': token
                    }
                )
            except User.DoesNotExist:
                messages.add_message(self.request, messages.WARNING, 'El Token es inválido')
                return redirect('/')
        else:
            messages.add_message(self.request, messages.WARNING, 'Token no enviado')
            return redirect('/')

    def post(self, request, *args, **kwargs):
        current_site = get_current_site(request)
        try:
            new_password_1 = request.POST.get('new_password_1', None)
            new_password_2 = request.POST.get('new_password_2', None)
            user = User.objects.get(token=request.POST['token'])
            if new_password_1 and new_password_2:
                if new_password_1 != new_password_2:
                    messages.add_message(self.request, messages.WARNING,
                                         'Las contraseñas no coinciden')
                    return redirect("http://%s%s?token=%s" % (current_site, reverse('password-set'),
                                                              request.POST['token']))
                else:
                    user.set_password(new_password_1)
                    user.token = request.POST['token']
                    user.save()
                    messages.add_message(self.request, messages.SUCCESS,
                                         'Contraseña actualizada correctamente. Ahora puedes iniciar sesión desde la aplicación')

            return redirect('/')
        except User.DoesNotExist:
            messages.add_message(self.request, messages.SUCCESS, 'Usuario no existe')
            return redirect("http://%s%s?token=%s" % (current_site, reverse('password-set'),
                                                      request.POST['token']))


class ForgetPassword(APIView):
    """
    """

    serializer_class = CustomerSerializer
    permission_classes = ()

    def post(self, request, format=None):
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        if user:
            # return Response({'error': 'El correo ya se encuentra registrado, por favor inicia sesión'},
            #                  status=status.HTTP_400_BAD_REQUEST)

            current_site = Site.objects.get_current()
            url = '{0}{1}/?token={2}'.format(current_site, settings.URL_SET_PASSWORD, user.token)
            send_email(
                subject="Recuperación contraseña Quality Seguros",
                ctx={
                        'title': "QUALITY Seguros - Recuperación de contraseña",
                        'message': "Has solicitado recuperar tu contraseña en Quality Seguros. Por favor sigue el siguiente link para crear tu nueva contraseña.", 
                        'url': url,
                },
                to_email=email
            )
            return Response({'success': 'Hemos enviado las instrucciones para que recuperes tu contraseña.'}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'El correo que ingresaste no ha sido encontrado en la base de datos. Intenta nuevamente'}, status=status.HTTP_400_BAD_REQUEST)

    