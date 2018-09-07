from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework.decorators import api_view

from ...serializers import (
    InsureranceSerializer
)

from insurances.models import Insurance


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