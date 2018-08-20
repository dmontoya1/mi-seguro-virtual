from django.db import models

from .insurance_category import InsuranceCategory


class Insurance(models.Model):
    """Almacena los seguros para la venta
    """

    category = models.OneToOneField(
        InsuranceCategory,
        on_delete=models.CASCADE,
        help_text='Enlace a la categoria del seguro',
        verbose_name='Categoria seguro'
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )

    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'

    def __str__(self):
        return self.name