from django.contrib import admin
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('sign_up/', views.CustomerViewSet.as_view(), name='sing_up'),
    path('login/', views.ObtainJWTView.as_view(), name='login'),
    path('profile/<int:pk>/', views.InfluencerUpdate.as_view(), name='influencer_update'),
    path('profile/<int:pk>/bank', views.InfluencerBankUpdate.as_view(), name='influencer_bank_update'),
    path('change-email/', views.UserChangeEmail.as_view(), name='user_change_email'),
    path('change-password/', views.UserChangePassword.as_view(), name='user_change_password'),
    path('customer/', views.CustomerDetail.as_view(), name='customer_datail'),
    path('password-set/', views.PasswordCreateView.as_view(), name='password-set'),
    path('password-reset/', views.ForgetPassword.as_view(), name='forget-password'),
]