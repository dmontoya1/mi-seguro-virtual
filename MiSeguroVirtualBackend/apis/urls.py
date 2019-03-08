from django.urls import path, include
from django.contrib import admin

from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

from rest_framework import routers

router = routers.DefaultRouter()

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('insurances/', include('insurances.urls', namespace='insurances'), name='insurances'),
    path('benefits/', include('benefits.urls', namespace='benefits'), name='benefits'),
    path('manager/', include('manager.urls', namespace='manager'), name='manager'),
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]
