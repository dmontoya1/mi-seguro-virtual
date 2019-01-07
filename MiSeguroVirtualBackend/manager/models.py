# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Police(models.Model):
    """
    clase para las politicas de la plataforma
    """

    TERMINOS_CONDICIONES = 'TC'
    POLITICAS_PRIVACIDAD = 'PP'

    POLICE_TYPE = (
        (TERMINOS_CONDICIONES, 'Términos y condiciones'),
        (POLITICAS_PRIVACIDAD, 'Políticas de privacidad'),
    )

    name = models.CharField("Nombre", max_length=50)
    text = models.TextField("Texto")
    police_type = models.CharField("Tipo de Política", max_length=2, choices=POLICE_TYPE,
                                   unique=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = "Politica"
