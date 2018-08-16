from django.db import models
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
        max_length=13,
        default=None
    )
    email = models.EmailField(
        'Correo electronico'
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


class AuthorizedPoint(models.Model):
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
    insurer = models.OneToOneField(
        Insurer,
        on_delete=models.CASCADE,
        help_text='Enlace a la aseguradora',
        verbose_name='Aseguradora',
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
    effective_date = models.DateField(
        'Fecha de vigencia',
        default=None
    )    

