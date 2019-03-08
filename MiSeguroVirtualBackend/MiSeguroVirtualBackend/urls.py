from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='insurances API')

urlpatterns = [
    path('schema/', schema_view),
    path('jet/', include('jet.urls', namespace='jet'), name='jet'),
    path('api/', include('apis.urls', namespace='api'), name='api'),
    path('admin/', admin.site.urls),
    path('', include('webclient.urls', namespace='webclient'), name='webclient'),
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('accounts/',include('allauth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
