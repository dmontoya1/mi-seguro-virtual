from django.contrib import admin
from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('terms-and-conditions/', views.TermsAndConditions.as_view(), name='terms-and-conditions'),
    path('privacy-policies/', views.PrivacyPolicies.as_view(), name='privacy-policies'),
]