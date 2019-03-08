
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Benefits
from .serializers import BenefitsSerializer


class BenefitsList(generics.ListAPIView):
    """
    """

    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    permission_classes = (AllowAny, )
