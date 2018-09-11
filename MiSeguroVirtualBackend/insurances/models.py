from django.db import models
from django.utils import timezone

from dateutil.relativedelta import relativedelta
from datetime import date, timedelta

from users.models import Broker, Customer


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
    brokers = models.ManyToManyField(
        Broker,
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
    PROCESS = 'PR'
    APPROVED = 'AP'

    STATUS_CHOICES = (
        (PENDING, 'Pendiente'),
        (PROCESS, 'En proceso'),
        (APPROVED, 'Aprobado')
    )

    insurance = models.ForeignKey(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Enlace al seguro',
        verbose_name='Seguro'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        help_text='Enlace al cliente',
        verbose_name='Cliente'
    )
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE,
        verbose_name='Corredores',
        default=''

    )
    adviser_code = models.CharField(
        'Codigo asesor',
        max_length=15,
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    state = models.CharField(
        'Estado',
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    request_date = models.DateField(
        'Fecha de solicitud'
    )

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


class CustomerPolicy(models.Model):
    """Almacena las polizas que caragan los corredores
    para cada uno de sus clientes
    """

    image = models.ImageField(
        'Imagen',
        upload_to = 'Polizas',
        blank=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        default = None
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
    expiration_date = models.DateField(
        default = timezone.now() + timezone.timedelta(days=1) + relativedelta(years=1),
        verbose_name="Fecha de vencimiento"
    )
    effective_date = models.DateField(
        default= timezone.now,
        verbose_name="Fecha inicio de vigencia"
    )

    class Meta:
        verbose_name = 'Póliza cliente'
        verbose_name_plural = 'Póliza clientes'
    

    def save(self, *args, **kwargs):
        self.expiration_date = self.effective_date + timezone.timedelta(days=1) + relativedelta(years=1)
        super(CustomerPolicy, self).save(*args, **kwargs)