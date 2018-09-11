from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User

from rest_framework.decorators import api_view

from ...serializers import (
    CustomerPolicySerializer
)

from insurances.models import CustomerPolicy
from users.models import Customer


class CusotmerPolicyDetail(APIView):
    serializer_class = CustomerPolicySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, format=None):
        try:
            username = str(request.user)
            user = User.objects.get(username=username)
            customer = Customer.objects.get(user=user)
            policy = CustomerPolicy.objects.filter(customer=customer)
            print(policy)
            serializer = CustomerPolicySerializer(policy, many=True)
            return Response(dict(status='done', details=serializer.data), status=200)

        except Exception as e:
            return Response(dict(status='error', details=str(e)), status=400)