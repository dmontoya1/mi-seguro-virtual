from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ...serializers import RequestSerializer
from insurances.models import InsuranceRequest

class RequestViewSet(APIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    #permission_classes=()

    def post(self, request, format=None):
        ip_user = get_client_ip(request)
        terms_date = timezone.now()
        user = dict(username=request.data['username'], first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], password=request.data['password'])
        user_data = dict(document_number=request.data['document_number'], cellphone_number=request.data['cellphone_number'], user=user)
        

        serializer = CustomerSerializer(data=user_data)

        try:
            if serializer.is_valid(raise_exception=True):
                customer = serializer.save()
                TermsAcceptanceLogs.objects.create(customer=customer , ip_address=ip_user, Acceptance_date=terms_date )
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)
