from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from apis.viewsets import (
    InsuranceList,
    InsuranceDetail,
    CustomerViewSet,
    ObtainJWTView,
    RequestViewSet,
    CusotmerPolicyDetail
)

schema_view = get_schema_view(title='insurances API')

urlpatterns = [
	path(r'schema/', schema_view),


    path('admin/', admin.site.urls),
    path(r'lista-seguros/', InsuranceList.as_view(), name='insurance_list'),
    path(r'seguro/detail/', InsuranceDetail.as_view(), name='insurance_detail'),
    path(r'sign_up/', CustomerViewSet.as_view(), name='sing_up'),
    path(r'login/', view=ObtainJWTView.as_view(), name='login'),
    path(r'insurance/request/', view=RequestViewSet.as_view(), name='request'),
    path(r'customer/policy/detail/', view=CusotmerPolicyDetail.as_view(), name='policy_detail')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)
