# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Police
from .serializers import PoliceSerializer


class TermsAndConditions(generics.ListAPIView):
    """
    Api para obtener terminos y condiciones
    """

    permission_classes = (AllowAny,)
    queryset = Police.objects.filter(police_type='TC')
    serializer_class = PoliceSerializer


class PrivacyPolicies(generics.ListAPIView):
    """
    Api para obtener politicas de privacidad
    """

    permission_classes = (AllowAny,)
    queryset = Police.objects.filter(police_type='PP')
    serializer_class = PoliceSerializer
