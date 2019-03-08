# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from fcm_django.models import FCMDevice

from insurances.models import UserPolicy

@receiver(post_save, sender=UserPolicy)
def send_email_to_customer(sender, **kwargs):
    if kwargs.get('created') is True:
        instance = kwargs.get('instance')
        try:
            user = instance.insurance_request.client
        except Exception as e:
            print (e)
            user = instance.client
        subject, from_email, to = 'Esta listo tu seguro', settings.EMAIL_USER, user.email
        try:
            insurance = instance.insurance_request.insurance
        except:
            insurance = instance.insurance
        
        text_content = 'Ya está listo tu seguro {}. Ingresa a tu aplicacion para que puedas visualizarlo'.format(insurance)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        if insurance.name == 'SOAT':
            msg.attach('seguro.pdf', instance.insurance_file.read(),  'application/pdf')
        msg.send()
        try:
            devices = FCMDevice.objects.filter(user=user)
            devices.send_message(
                title='Se ha generado tu seguro',
                body='Ya está listo tu seguro {}. Ve a la seccion "Mis seguros" para ver los detalles'.format(insurance),
                sound="default",
            )
        except:
            pass
        if instance.adviser_mail:
            subject, from_email, to = 'Esta listo el seguro del cliente {}'.format(user), settings.EMAIL_USER, user.email
            text_content = 'Ya está listo el seguro {} del cliente {}.'.format(instance.insurance_request.insurance, user)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            if instance.insurance.name == 'SOAT':
                msg.attach('seguro.pdf', instance.insurance_file.read(),  'application/pdf')
            msg.send()
