from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


from users.models import User


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
    
    def __unicode__(self):
        return '%s' % (self.name)


class Insurance(models.Model):
    """Almacena los seguros para la venta
    """

    category = models.ForeignKey(
        InsuranceCategory,
        on_delete=models.CASCADE,
        help_text='Enlace a la categoria del seguro',
        verbose_name='Categoria seguro'
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'   


    def __str__(self):
        return self.name


class Insurer(models.Model):
    """Almacena las aseguradoras
    """
    
    insurances = models.ManyToManyField(
        Insurance,
        verbose_name='Seguros',

    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Corredores'
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )
    cellphone_number = models.CharField(
        'Numero de celular',
        max_length=13
    )
    email = models.EmailField(
        'Correo electronico'
    )
    active= models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Aseguradora'
        verbose_name_plural = 'Aseguradoras'


    def __str__(self):
        return self.name


class PointOfSale(models.Model):
    """Almacena los puntos de venta autorizados para los seguros
    """

    name = models.CharField(
        'Nombre',
        max_length=50
    )
    mail = models.EmailField(
        'Correo Electronico'
    )
    cellphone_number = models.CharField(
        'Numero de celular',
        max_length=13
    )
    code = models.CharField(
        'Codigo',
        max_length=10
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Corredores'
    )

    class Meta:
        verbose_name = 'Punto autorizado'
        verbose_name_plural = 'Puntos autorizados'


    def __str__(self):
        return self.name


class InsuranceRequest(models.Model):
    """Almacena las solicitudes de seguros hechas por los clientes
    """
    PENDING = 'PE'
    EXPIRE = 'EX'
    APPROVED = 'AP'
    PROCESS = 'PR'
    CURRENT = 'CU'

    STATUS_CHOICES = (
        (PENDING, 'Pendiente'),
        (EXPIRE, 'Vencido'),
        (PROCESS, 'En proceso'),
        (APPROVED, 'Aprobado'),
        (CURRENT, 'Vigente'),
    )

    insurance = models.ForeignKey(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Enlace al seguro',
        verbose_name='Seguro'
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='Enlace al cliente',
        verbose_name='Cliente',
        related_name='related_insurances_client'
    )
    broker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Corredores',
        default='',
        related_name='related_insurances_broker',
    )
    adviser_code = models.CharField(
        'Codigo asesor',
        max_length=15,
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    status = models.CharField(
        'Estado',
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    request_date = models.DateField(
        'Fecha de solicitud'
    )

    def __str__(self):
        return "Solicitud del cliente %s" % (self.client)

    class Meta:
        verbose_name = 'Historial solicitud'
        verbose_name_plural = 'Historial solicitudes'


class DocumentsRequest(models.Model):
    """Alamcena las imagenes de los documentos asociados a
    solicitud
    """
    insurance_request = models.OneToOneField(
        InsuranceRequest,
        on_delete=models.CASCADE,
        verbose_name='Solicitud'
    )
    property_card = models.ImageField(
        'Imagen',
        upload_to = 'Solicitudes/tarjetas',
        blank=True
    )
    drive_license = models.ImageField(
        'Imagen',
        upload_to = 'Solicitudes/licencias',
        blank=True
    ) 

    def __str__(self):
        return "Documentos de %s" % (self.insurance_request)

    class Meta:
        verbose_name = "Documento de la solicitud"
        verbose_name_plural = "Documentos de la solicitud"


class UserPolicy(models.Model):
    """Almacena las polizas que caragan los corredores
    para cada uno de sus clientes
    """

    insurance_request = models.OneToOneField(
        InsuranceRequest,
        on_delete=models.CASCADE,
        verbose_name='Póliza del cliente'
    )
    insurance_file = models.FileField(
        'Documento del seguro',
        upload_to = 'Polizas',
        blank=True
    ) 
    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        help_text='Enlace a la aseguradora',
        verbose_name='Aseguradora'
    )
    licensed_plate =models.CharField(
        'placa',
        max_length=8,
        default='###-###'
    )
    adviser_mail = models.EmailField(
        'Correo asesor',
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    effective_date = models.DateField(
        default= timezone.now,
        verbose_name="Fecha inicio de vigencia"
    )
    expiration_date = models.DateField(
        verbose_name="Fecha de vencimiento",
        auto_now_add=False
    )

    class Meta:
        verbose_name = 'Póliza cliente'
        verbose_name_plural = 'Póliza clientes'

    def __str__(self):
        return "Póliza %s del cliente %s" % (self.insurance_request.insurance, self.insurance_request.client)

    
    def clean(self, *args, **kwargs):
        " Make sure expiry time cannot be in the past "
        d = self.effective_date
        dt = datetime(d.year, d.month, d.day)
        if dt <= datetime.now():
            raise ValidationError('La fecha de inicio de la vigencia debe ser mayor a hoy')
        else:
            self.expiration_date = self.effective_date + relativedelta(years=1) - timezone.timedelta(days=1) 
            super(UserPolicy, self).save(*args, **kwargs)
