from django.db import models

from .insurance import Insurance
from MiSeguroVirtualBackend.users.models import Broker


class Insurer(models.Model):
    """Almacena las aseguradoras
    """

    insurances = models.ManyToManyField(
        Insurance,
        verbose_name='Seguros',

    )
    brokers = models.ManyToManyField(
        Broker,
        verbose_name='Corredores'

    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )
    cellphone_number = models.CharField(
        'Numero de celular',
        max_length=13,
        default=None
    )
    email = models.EmailField(
        'Correo electronico'
    )
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Aseguradora'
        verbose_name_plural = 'Aseguradoras'


    def __str__(self):
        return self.name