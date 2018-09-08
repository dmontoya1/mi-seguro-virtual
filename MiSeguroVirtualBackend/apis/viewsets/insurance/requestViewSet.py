from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User

from ...serializers import RequestSerializer
from insurances.models import InsuranceRequest, Insurance
from users.models import Customer


from datetime import date

class RequestViewSet(APIView):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, format=None):
        
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
                return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:

            return Response(dict(status='error', details=str(e)), status=400)
