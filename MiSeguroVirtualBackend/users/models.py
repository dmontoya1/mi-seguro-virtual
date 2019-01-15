
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    """

    CEDULA = 'CC'
    TARJETA = 'TI'
    PASAPORTE = 'PA'
    CEDULAE = 'CE'

    CORREDOR = 'CO'
    CLIENTE = 'CL'
    INFLUENCER = 'IN'

    USER_TYPE = (
        (CORREDOR, 'Corredor de Seguros'),
        (INFLUENCER, 'Influenciador'),
        (CLIENTE, 'Cliente')
    )

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

    user_type = models.CharField(
        "Tipo de usuario",
        choices=USER_TYPE,
        max_length=2
    )
    phone_number = models.CharField(
        'Número de celular',
        max_length=13
    )
    logo = models.ImageField(
        'Imagen',
        upload_to='logotipos',
        blank=True
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=20,
        choices=DOCUMENT_CHOICES,
        help_text = 'Tipo de documento de identidad'
    )
    document_id = models.CharField(
        'Numero de documento',
        max_length=15
    )
    bank = models.CharField(
        "Banco",
        max_length=255,
        blank=True, null=True
    )
    account_type = models.CharField(
        "Tipo de cuenta bancaria",
        max_length=2,
        choices=ACCOUNT_TYPE,
        blank=True, null=True
    )
    account_number = models.CharField(
        "Número de cuenta bancaria",
        max_length=50,
        blank=True, null=True
    )
    code = models.CharField(
        "Código de influencer",
        max_length=15,
        blank=True, null=True
    )
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = 'Usuario'


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

    def __str__(self):
        return "Log de términos de %s" % (self.user)


    class Meta:
        verbose_name = "Log de Términos"
        verbose_name_plural = "Logs de términos"
