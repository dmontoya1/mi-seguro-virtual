

from django.urls import path

from .views import BenefitsList


app_name = 'benefits'
urlpatterns = [
    path('list/', BenefitsList.as_view(), name='benefits_list'),
]
