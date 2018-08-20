from datetime import date, timedelta

from django.db import models
from django.utils import timezone

from .insurer import Insurer
from .insurance import Insurance


class CustomerPolicy(models.Model):
    """Almacena las polizas que caragan los corredores
    para cada uno de sus clientes
    """

    image = models.ImageField(
        'Imagen',
        blank=True
    )
    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        help_text='Enlace a la aseguradora',
        verbose_name='Aseguradora'
    )
    insurance = models.ForeignKey(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Enlace al seguro',
        verbose_name='Seguro',
        default=None
    )
    adviser_code = models.CharField(
        'Codigo asesor',
        max_length=15,
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    adviser_mail = models.EmailField(
        'Correo asesor',
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    effective_date = models.DateField(
        editable=False,
        verbose_name="Fecha de vigencia"
    )

    class Meta:
        verbose_name = 'Póliza cliente'
        verbose_name_plural = 'Póliza clientes'


    def save(self, *args, **kwargs):
        self.effective_date = timezone.now() + timezone.timedelta(days=1)
        super(CustomerPolicy, self).save(*args, **kwargs)