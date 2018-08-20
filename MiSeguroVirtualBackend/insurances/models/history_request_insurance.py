from django.db import models

from .insurance import Insurance
from .authorized_point import AuthorizedPoint

from MiSeguroVirtualBackend.users.models import (
    Broker,
    Customer
)

class HistoryRequestInsurance(models.Model):

    """Almacena las solicitudes de seguros hechas por los clientes
    """
    PENDING = 'PE'
    PROCESS = 'PR'
    APPROVED = 'AP'

    STATUS_CHOICES = (
        (PENDING, 'Pendiente'),
        (PROCESS, 'En proceso'),
        (APPROVED, 'Aprobado')
    )

    insurance = models.OneToOneField(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Enlace al seguro',
        verbose_name='Seguro',
        default=None
    )
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        help_text='Enlace al cliente',
        verbose_name='Cliente',
        default=None
    )
    broker = models.OneToOneField(
        Broker,
        on_delete=models.CASCADE,
        help_text='Enlace al corredor',
        verbose_name='Corredor',
        default=None
    )
    authorized_point = models.OneToOneField(
        AuthorizedPoint,
        on_delete=models.CASCADE,
        help_text='Enlace al punto autorizado',
        verbose_name='Punto Autorizado',
        default=None
    )
    state = models.CharField(
        'Estado',
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    request_date = models.DateField(
        'Fecha de solicitud',
        default=None
    )

    class Meta:
        verbose_name = 'Historial solicitud'
        verbose_name_plural = 'Historial solicitudes'
