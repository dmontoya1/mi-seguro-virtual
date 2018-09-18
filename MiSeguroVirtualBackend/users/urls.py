from django.contrib import admin
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('sign_up/', views.CustomerViewSet.as_view(), name='sing_up'),
    path('login/', views.ObtainJWTView.as_view(), name='login'),
    path('profile/<int:pk>/', views.InfluencerUpdate.as_view(), name='influencer_update'),
    path('change-email/', views.UserChangeEmail.as_view(), name='user_change_email'),
    path('change-password/', views.UserChangePassword.as_view(), name='user_change_password'),

]