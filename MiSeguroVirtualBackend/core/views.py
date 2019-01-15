# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
from django.template import loader

def send_email(subject, ctx, to_email):
    """
    Función para enviar el correo electrónico a un usuario creado por el administrador
    para que éste pueda crear su contraseña para acceder al sitio
    """

    body = loader.render_to_string('email/base_email.html', ctx)
    message = EmailMessage(subject, body, settings.EMAIL_USER, [to_email])
    message.content_subtype = 'html'
    message.send()
