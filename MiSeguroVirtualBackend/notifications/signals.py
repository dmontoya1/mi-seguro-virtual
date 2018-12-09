# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from fcm_django.models import FCMDevice
from users.models import User
from .models import Notification

@receiver(post_save, sender=Notification)
def notification_create_verify(sender, **kwargs):
    """
    Función para enviar una notificación push cuando una notificación
    es creada
    """
    instance = kwargs.get('instance')
    if kwargs.get('created') is True:
        if instance.user is None:
            devices = FCMDevice.objects.all()
            devices.send_message(
                title=instance.title,
                body=instance.description,
                sound="default",
            )
        else:
            try:
                devices = FCMDevice.objects.filter(user=instance.user)
                devices.send_message(
                    title=instance.title,
                    body=instance.description,
                    sound="default",
                )
            except Exception as e:
                print (e)
                pass
