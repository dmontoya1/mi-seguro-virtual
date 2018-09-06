from django.db import models
from django.contrib.auth.models import User


class Broker(models.Model):
    """Almacena los corredores de seguros.
    """

    """insurances = models.ManyToManyField(
        'insurances.Insurance',
        verbose_name='Seguros'

    )"""
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
    logo = models.ImageField(
        'Imagen',
        upload_to='logotipos',
        blank=True
    )

    class Meta:
        verbose_name = 'Corredor'
        verbose_name_plural = 'Corredores'
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    """almacena los clientes que desean adquirir seguros
    """
    CEDULA = 'CC'
    TARJETA = 'TI'
    PASAPORTE = 'PA'
    CEDULAE = 'CE'

    DOCUMENT_CHOICES = (
        (CEDULA, 'Cedula'),
        (TARJETA, 'Tarjeta de identidad'),
        (PASAPORTE, 'Pasaporte'),
        (CEDULAE, 'Cedula de extrajeria')
    )

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        help_text='Enlace al usuario',
        verbose_name='Usuario',
        null=True,
        blank=True
    )
    cellphone_number = models.CharField(
        'Número de celular',
        max_length=13
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=20,
        choices=DOCUMENT_CHOICES,
        help_text = 'Tipo de documento de identidad'
    )
    document_number = models.CharField(
        'Numero de documento',
        max_length=15
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.document_number


    def get_full_name(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name

    
    def get_short_name(self):
        return self.user.first_name

class TermsAcceptanceLogs(models.Model):
    """Almacena los terminos y condiciones de un usuario determinado
    """
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Cliente'
    )
    Acceptance_date = models.DateField(
        'Fecha de solicitud'
    )
    ip_address = models.CharField(
        'IP de aceptacion del cliente',
        max_length=20
    )