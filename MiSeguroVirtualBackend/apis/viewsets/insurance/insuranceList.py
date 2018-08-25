from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view

from ...serializers import (
    InsureranceSerializer
)

from insurances.models import Insurance


class InsuranceList(APIView):

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