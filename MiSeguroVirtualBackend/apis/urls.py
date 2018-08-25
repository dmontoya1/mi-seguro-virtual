from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from MiSeguroVirtualBackend.apis.viewsets import (
    InsuranceList,
    CustomerViewSet    
)

router = routers.DefaultRouter()

urlpatterns = [
    path(r'^', include(router.urls)),

    path(r'^lista-seguros/$', InsuranceList.as_view(), name='insurance_list'),
    path(r'^personas/$', CustomerViewSet.as_view(), name='registro'),
]
