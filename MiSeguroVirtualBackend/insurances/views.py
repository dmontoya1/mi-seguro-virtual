
from datetime import date

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.utils import timezone

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.models import User

from .models import UserPolicy, Insurance, DocumentsRequest, InsuranceRequest, DomiRequestInsurer
from .serializers import (
    UserPolicySerializer, 
    InsuranceSerializer, 
    RequestSerializer, 
    RequestGetSerializer,
    InsuranceDetailSerializer,
    InsuranceRequestSerializer
)


class UserPolicyDetail(generics.ListAPIView):
    serializer_class = UserPolicySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        queryset = UserPolicy.objects.filter(
            Q(client=self.request.user) |
            Q(insurance_request__client=self.request.user)
        )
        if queryset.exists():
            return queryset
        return ''


class InsuranceList(generics.ListAPIView):
    serializer_class = InsuranceSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Insurance.objects.filter(is_active=True).order_by('id')


class InsuranceDetail(generics.RetrieveAPIView):
    serializer_class = InsuranceDetailSerializer
    permission_classes = (AllowAny,)
    queryset = Insurance.objects.all()


class RequestViewSet(APIView):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        
        property1 = request.data['property1']
        property2 = request.data['property2']
        try:
            oldSoat = request.data['oldSoat']
        except:
            oldSoat = None

        request_date = date.today()
        username = request.user
        name = request.data['name']
        adviser_code = request.data['adviser_code']
        fisico = request.data['fisico']
        optionId = request.data['optionId']
        price = request.data['price']

        user = User.objects.get(username=username)
        insurance = Insurance.objects.filter(name=name).first()
        # broker = User.objects.get(username='apptitud')

        try:
            request_obj = InsuranceRequest(
                status=InsuranceRequest.PENDING,
                request_date=request_date,
                client=user,
                insurance=insurance,
                adviser_code=adviser_code,
                price=price
            )
            request_obj.save()
        
            # document_request = DocumentsRequest.objects.create(insurance_request=request_insurance, property_card=foto1, drive_license=foto2)
            # document_request.save()
            sendMail(username, property1, property2, oldSoat, optionId, fisico)
            return Response({'detail':'Solicitud creada exitosamente'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            print ("EXception")
            print (e)
            return Response({'detail':'Ha ocurrido un error al crear la solicitud'}, status=status.HTTP_400_BAD_REQUEST)


class Requests(generics.ListAPIView):
    """Lista de solicitudes de los usuarios
    """

    model = InsuranceRequest
    serializer_class = InsuranceRequestSerializer


    def get_queryset(self):
        return InsuranceRequest.objects.filter(client=self.request.user)


class RequestDetail(generics.RetrieveAPIView):
    """Detalle de una solicitud
    """

    model = InsuranceRequest
    serializer_class = InsuranceRequestSerializer
    queryset = InsuranceRequest.objects.all()


class UploadPaymentProof(APIView):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        
        paymentProof = request.data['payment']
        request_code = request.data['request_code']
        
        try:
            request_obj = InsuranceRequest.objects.get(request_code=request_code)
        except InsuranceRequest.DoesNotExists:
            request_obj = None
        
        if request_obj:
            request_obj.payment_proof = paymentProof
            request_obj.status = InsuranceRequest.PROCESS
            request_obj.save()
            sendPaymentMail(request_obj.client.username, request_obj, paymentProof)
        
        
            return Response({
                'detail': 'Recibo de pago enviado exitosamente'
            }, status=status.HTTP_200_OK)

        return Response({
                'detail': 'Ha ocurrido un error al recibir tu recibo de pago'
            }, status=status.HTTP_400_BAD_REQUEST)


class DomiRequestInsuranceCreate(APIView):
    """ Crea los datos de recogida del dinero cuando van a pagar en efectivo
    """

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        
        request_id = request.data['request_id']
        address = request.data['address']
        pickup_date = request.data['pickup_date']
        pickup_time = request.data['pickup_time']

        request_insurance = InsuranceRequest.objects.filter(id=request_id).first()

        try:
            domi = DomiRequestInsurer(
                request_insurance = request_insurance,
                address=address,
                pickup_date=pickup_date,
                pickup_time=pickup_time,
            )
            domi.save()
        
            # sendMail(username, property1, property2, oldSoat, optionId, fisico)
            return Response({'detail':'Solicitud creada exitosamente'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            print ("EXception")
            print (e)
            return Response({'detail':'Ha ocurrido un error al crear la solicitud'}, status=status.HTTP_400_BAD_REQUEST)


def sendMail(username, doc1, doc2, oldSoat, optionId, fisico):
    subject, from_email = 'Solicitud de seguro', settings.EMAIL_USER
    text_content = 'Acabas de recibir una nueva solicitud de seguro del usuario {}. El codigo del seguro es {}. Este usuario ha \
    elegido la option de enviar el SOAT en fisico como {}. '.format(str(username), optionId, fisico)
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['yo@diegonaranjo.co', 'alukas@segurosquality.com', 'soporte@segurosquality.com'])
    msg.attach('propiedad1.jpeg', doc1.read(), 'image/jpeg')
    msg.attach('propiedad2.jpeg', doc2.read(), 'image/jpeg')
    if oldSoat:
        msg.attach('Soat-antetior.jpeg', oldSoat.read(), 'image/jpeg')
    msg.send()

def sendPaymentMail(username, request_obj, img):
    subject, from_email = 'Recibo de pago SOAT', settings.EMAIL_USER
    text_content = 'Acabas de recibir el recibo de pago del SOAT con codigo {} del usuario {}. '.format(request_obj.request_code, request_obj.client.username)
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['yo@diegonaranjo.co', 'alukas@segurosquality.com', 'soporte@segurosquality.com'])
    msg.attach('ReciboPago.jpeg', img.read(), 'image/jpeg')
    msg.send()
