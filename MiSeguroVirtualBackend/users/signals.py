# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from fcm_django.models import FCMDevice

from core.views import send_email

from .models import User

@receiver(post_save, sender=User)
def new_users_verify(sender, **kwargs):
    instance = kwargs.get('instance')
    current_site = Site.objects.get_current()
    url = '{0}{1}/?token={2}'.format(current_site, settings.URL_SET_PASSWORD, instance.token)
    if kwargs.get('created') is True:
        send_email(
        subject="Activación cuenta Quality Seguros",
        ctx={
                'title': "QUALITY Seguros - Activación de cuenta",
                'name': 'Test',
                'message': "Has sido registrado en Quality Seguros. Para crear tu contraseña, por favor accede el siguiente link:", 
                'url': url,
        },
        to_email=instance.username
        )