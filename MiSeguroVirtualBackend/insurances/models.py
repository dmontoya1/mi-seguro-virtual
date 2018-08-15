from django.db import models
from users.models import Broker


class InsuranceCategory(models.Model):
    """Almacena las categorias que tendran los seguros
    """

    name = models.CharField(
        'Nombre',
        max_length=50
    )

    class Meta:
        verbose_name = 'Categoria de seguro'
        verbose_name_plural = 'Categoria de seguros'
    
    def __str__(self):
        return self.name


class Insurer(models.Model):
    """Almacena las aseguradoras
    """
    brokers = models.ManyToManyField(
        Broker,
        help_text='Enlace a los corredores, ',
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
    
    def __str__(self):
        return self.name


class Insurance(models.Model):
    """Almacena los seguros para la venta
    """
    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        help_text='Enlace a la aseguradora',
        verbose_name='Aseguradora',
        default=None

    )
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
        
    def __str__(self):
        return self.name


class CustomerInsurance(models.Model):
    """Almacena las pólizas creadas
    """

    insurance = models.OneToOneField(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Enlace a el seguro'
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )

    class Meta:
        verbose_name = 'Seguro de usuario'
        verbose_name_plural = 'Seguros de usuario'

    def __str__(self):
        return self.name