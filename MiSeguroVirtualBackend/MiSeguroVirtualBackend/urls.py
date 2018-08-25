from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from apis.viewsets import (
    InsuranceList,
    CustomerViewSet    
)

schema_view = get_schema_view(title='insurances API')

urlpatterns = [
	path(r'schema/', schema_view),


    path('admin/', admin.site.urls),
    path(r'lista-seguros/', InsuranceList.as_view(), name='insurance_list'),
    path(r'registro/', CustomerViewSet.as_view(), name='registro'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)
