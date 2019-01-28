
# from allauth.account.views import SignupView, LoginView, PasswordResetView

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views


app_name = 'webclient'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('next/', views.TestView.as_view(), name='test'),
    path('login/', views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('policies/<str:type>/', views.PoliciesView.as_view(), name='policies'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profites/', views.InfluencerProfits.as_view(), name='influencer_profits'),
]