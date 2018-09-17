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
        (CEDULA, 'Cédula de Ciudadanía'),
        (TARJETA, 'Tarjeta de identidad'),
        (PASAPORTE, 'Pasaporte'),
        (CEDULAE, 'Cédula de extrajería')
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
        return self.user.username


    def get_full_name(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name

    
    def get_short_name(self):
        return self.user.first_name


class Influencer(models.Model):
    """Almacena los influenciadores 
    """

    CEDULA = 'CC'
    TARJETA = 'TI'
    PASAPORTE = 'PA'
    CEDULAE = 'CE'

    AHORROS = 'AH'
    CORRIENTE = 'CO'

    DOCUMENT_CHOICES = (
        (CEDULA, 'Cédula de Ciudadanía'),
        (TARJETA, 'Tarjeta de identidad'),
        (PASAPORTE, 'Pasaporte'),
        (CEDULAE, 'Cédula de extrajería')
    )

    ACCOUNT_TYPE = (
        (AHORROS, 'Ahorros'),
        (CORRIENTE, 'Corriente')
    )

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        help_text='Enlace al usuario',
        verbose_name='Usuario',
        null=True,
        blank=True
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=DOCUMENT_CHOICES,
        help_text = 'Tipo de documento de identidad'
    )
    document_number = models.CharField(
        'Numero de documento',
        max_length=15
    )

    phone_number = models.CharField(
        "Número telefónico",
        max_length=10
    )
    bank = models.CharField(
        "Banco",
        max_length=255
    )
    account_type = models.CharField(
        "Tipo de cuenta bancaria",
        max_length=2,
        choices=ACCOUNT_TYPE
    )
    account_number = models.CharField(
        "Número de cuenta bancaria",
        max_length=50
    )
    code = models.CharField(
        "Código de influencer",
        max_length=15
    )

    def __str__(self):
        return self.user.username


    def get_full_name(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name

    
    def get_short_name(self):
        return self.user.first_name


class TermsAcceptanceLogs(models.Model):
    """Almacena los terminos y condiciones de un usuario determinado
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    Acceptance_date = models.DateField(
        'Fecha de solicitud',
        auto_now_add=True
    )
    ip_address = models.CharField(
        'IP de aceptacion del cliente',
        max_length=20
    )