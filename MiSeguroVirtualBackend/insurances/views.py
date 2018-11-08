
from datetime import date

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

from rest_framework import generics   
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.models import User

from .models import UserPolicy, Insurance, DocumentsRequest
from .serializers import (
    UserPolicySerializer, 
    InsuranceSerializer, 
    RequestSerializer, 
    RequestGetSerializer,
    InsuranceDetailSerializer
)


class UserPolicyDetail(APIView):
    serializer_class = UserPolicySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, format=None):
        try:
            policy = UserPolicy.objects.filter(insurance_request__client=request.user)
            if policy.exists():
                serializer = UserPolicySerializer(policy, many=True)
                return Response(dict(status='done', details=serializer.data), status=200)
            else:
                return Response(dict(status='error', details=str("No hay pólizas disponibles")), status=400)
        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)


class InsuranceList(generics.ListAPIView):
    serializer_class = InsuranceSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        return Insurance.objects.filter(is_active=True).order_by('id')


class InsuranceDetail(generics.RetrieveAPIView):
    serializer_class = InsuranceDetailSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Insurance.objects.all()


class RequestViewSet(APIView):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        
        foto1 = request.data['photo1']
        foto2 = request.data['photo2']

        # fs_1 = FileSystemStorage()
        # filename_1 = fs_1.save("Solicitudes/licencias/" + foto1.name, foto1)
        # photo1 = fs_1.save(filename_1)

        # fs_2 = FileSystemStorage()
        # filename_2 = fs_2.save("Solicitudes/licencias/" + foto2.name, foto2)
        # photo2 = fs_2.save(filename_2)

        request_date = date.today()
        username = request.user
        status = 'PR'
        name = request.data['name']
        adviser_code = request.data['adviser_code']

        user = User.objects.get(username=username)
        insurance = Insurance.objects.filter(name=name).first()
        broker = User.objects.get(username='apptitud')

        request = dict(
            status=status,
            request_date=request_date,
            client=user.pk,
            insurance=insurance.id,
            broker=broker.id,
            adviser_code=adviser_code
        )
        
        serializer = RequestSerializer(data=request)
        try:
            if serializer.is_valid(raise_exception=True):
                request_insurance = serializer.save()
                document_request = DocumentsRequest.objects.create(insurance_request=request_insurance, property_card=foto1, drive_license=foto2)
                document_request.save()
                sendMail(username, foto1, foto2)
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)


def sendMail(username, foto1, foto2):
    subject, from_email, to = 'Solicitud de seguro', settings.EMAIL_USER, 'dmontoya.web@gmail.com'
    text_content = 'Acabas de recibir una nueva solicitud de seguro del usuario ' + str(username)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach('licencia.jpeg', foto1.read(), 'image/jpeg')
    msg.attach('tarjeta.jpeg', foto2.read(), 'image/jpeg')
    msg.send()
