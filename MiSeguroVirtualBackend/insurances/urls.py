from django.contrib import admin
from django.urls import path

from . import views

# schema_view = get_schema_view(title='insurances API')

app_name = 'insurances'
urlpatterns = [
    path('', views.InsuranceList.as_view(), name='insurance_list'),
    path('detail/<int:pk>/', views.InsuranceDetail.as_view(), name='insurance_detail'),
    path('insurance/request/', views.RequestViewSet.as_view(), name='request'),
    path('customer/policy/detail/', views.UserPolicyDetail.as_view(), name='policy_detail')
]