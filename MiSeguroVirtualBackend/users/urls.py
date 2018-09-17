from django.contrib import admin
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('sign_up/', views.CustomerViewSet.as_view(), name='sing_up'),
    path('login/', views.ObtainJWTView.as_view(), name='login'),

]