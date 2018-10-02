# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from insurances.models import UserPolicy
from .models import User

@receiver(post_save, sender=UserPolicy)
def send_email_to_customer(sender, **kwargs):
    if kwargs.get('created') is True:
        instance = kwargs.get('instance')
        user = instance.insurance_request.client
        subject, from_email, to = 'Esta listo tu seguro', settings.EMAIL_USER, user.email
        text_content = 'Ya está listo tu seguro {}. Puedes descargarlo en el archivo que te enviamos adjunto'.format(instance.insurance_request.insurance)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach('seguro.jpeg', instance.insurance_file.read(),  'image/jpeg')
        msg.send()

        if instance.adviser_mail:
            subject, from_email, to = 'Esta listo el seguro del cliente {}'.format(user), settings.EMAIL_USER, user.email
            text_content = 'Ya está listo el seguro {} del cliente {}. Puedes descargarlo en el archivo que te enviamos adjunto'.format(instance.insurance_request.insurance, user)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach('seguro.jpeg', instance.insurance_file.read(),  'image/jpeg')
            msg.send()
