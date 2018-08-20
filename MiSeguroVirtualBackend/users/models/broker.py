from django.db import models

from .user import User


class Broker(models.Model):
    """Almacena los corredores de seguros.
    """

    insurances = models.ManyToManyField(
        'insurances.Insurance',
        verbose_name='Seguros',
        blank=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text='Enlace al usuario',
        verbose_name='Usuario'
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )
    cellphone_number = models.CharField(
        'Número de celular',
        max_length=13
    )

    class Meta:
        verbose_name = 'Corredor'
        verbose_name_plural = 'Corredores'

    def __str__(self):
        return self.name