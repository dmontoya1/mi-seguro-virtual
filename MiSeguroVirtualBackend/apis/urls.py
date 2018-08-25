from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from MiSeguroVirtualBackend.apis.viewsets import (
    InsuranceList    
)

router = routers.DefaultRouter()

urlpatterns = [
    path(r'^', include(router.urls)),

    path(r'^lista-seguros/$', ClientList.as_view(), name='insurance_list'),
]
