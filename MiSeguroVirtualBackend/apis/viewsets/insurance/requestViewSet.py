from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User

from ...serializers import RequestSerializer
from insurances.models import InsuranceRequest, Insurance, DocumentsRequest
from users.models import Customer


from datetime import date

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

        user = User.objects.get(username=username)
        customer = Customer.objects.get(user=user.id)
        insurance = Insurance.objects.get(name=name)

    
        request = dict(state=state, request_date=request_date, customer=customer.id, insurance=insurance.id)
        
        serializer = RequestSerializer(data=request)

        try:
            if serializer.is_valid(raise_exception=True):
                request_insurance = serializer.save()
                document_request = DocumentsRequest.objects.create(insurance_request=request_insurance, property_card=foto1, drive_license=foto2)
                document_request.save()
                documents = document_request
                print("docuemntos", documents)
                sendMail(username, foto1, foto2)
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
