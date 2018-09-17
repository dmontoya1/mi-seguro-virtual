
from datetime import date

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.models import User

from .models import UserPolicy, Insurance, DocumentsRequest
from .serializers import UserPolicySerializer, InsureranceSerializer, RequestSerializer


class UserPolicyDetail(APIView):
    serializer_class = UserPolicySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, format=None):
        try:
            username = str(request.user)
            user = User.objects.get(username=username)
            policy = UserPolicy.objects.filter(user=user)
            print(policy)
            serializer = UserPolicySerializer(policy, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)


class InsuranceList(APIView):
    serializer_class = InsureranceSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)


    def get(self, request, format=None):
        try:
            insurances = Insurance.objects.all()
            size = len(insurances)
            insurances_list = []*size
            for insurance in insurances:
                if insurance.active:
                    insurances_list.append(insurance)

            serializer = InsureranceSerializer(insurances_list, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)


        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)


class InsuranceDetail(APIView):
    serializer_class = InsureranceSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)


    def get(self, request, format=None):
        try:
            name = self.request.query_params.get('name')
            insurances = Insurance.objects.filter(name=name)
            serializer = InsureranceSerializer(insurances, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)


class RequestViewSet(APIView):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        
        foto1 = request.data['photo1']
        foto2 = request.data['photo2']

        request_date = date.today()
        username = request.user
        state = 'PR'
        name = request.data['name']
        adviser_code = request.data['adviser_code']

        user = User.objects.get(username=username)
        insurance = Insurance.objects.get(name=name)
        broker = Broker.objects.get(name='Quality')

    
        request = dict(state=state, request_date=request_date, user=user.pk, insurance=insurance.id, broker=broker.id, adviser_code=adviser_code)
        
        serializer = RequestSerializer(data=request)

        try:
            if serializer.is_valid(raise_exception=True):
                request_insurance = serializer.save()
                document_request = DocumentsRequest.objects.create(insurance_request=request_insurance, property_card=foto1, drive_license=foto2)
                document_request.save()
                documents = document_request
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)


def sendMail(username, foto1, foto2):

    subject, from_email, to = 'Solicitud de seguro', settings.EMAIL_HOST_USER, 'jorgemsm12316@gmail.com'
    text_content = 'Acabas de recibir una nueva solicitud de seguro del usuario ' + str(username)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach('licencia.jpeg', foto1, 'image/jpeg')
    msg.attach('tarjeta.jpeg', foto2, 'image/jpeg')
    msg.send()
