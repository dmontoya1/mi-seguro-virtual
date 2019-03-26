from django.contrib import admin
from django.urls import path

from . import views


app_name = 'insurances'
urlpatterns = [
    path('', views.InsuranceList.as_view(), name='insurance_list'),
    path('detail/<int:pk>/', views.InsuranceDetail.as_view(), name='insurance_detail'),
    path('insurance/request/', views.RequestViewSet.as_view(), name='request'),
    path('customer/policy/detail/', views.UserPolicyDetail.as_view(), name='policy_detail'),
    path('requests/', views.Requests.as_view(), name='user_requests'),
    path('request-create/', views.AnswerCreate.as_view(), name='request_create'),
    path('upload-payment/', views.UploadPaymentProof.as_view(), name='upload_payment'),
    path('request/<int:pk>/', views.RequestDetail.as_view(), name='user_requests_detail'),
    path('request-domi/', views.DomiRequestInsuranceCreate.as_view(), name='create_domi'),
]