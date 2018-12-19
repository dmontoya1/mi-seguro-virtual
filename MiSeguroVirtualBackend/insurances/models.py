from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


from users.models import User


class Category(models.Model):
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


class Subcategory(models.Model):
    """Almacena las subcategorias que tendran los seguros
    """
    category = models.ForeignKey(
        Category,
        verbose_name="Categoría",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )

    class Meta:
        verbose_name = 'Subcategoría de seguro'
        verbose_name_plural = 'Subcategorías de seguros'
    

    def __str__(self):
        return '{} ({})'.format(self.name, self.category)


class Insurance(models.Model):
    """Almacena los seguros para la venta
    """

    category = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        help_text='Categoria del seguro',
        verbose_name='Categoria seguro'
    )
    name = models.CharField(
        'Nombre',
        max_length=100
    )
    is_active = models.BooleanField(
        'Activo?', 
        default=True
    )
    image = models.ImageField(
        'Imagen del seguro',
        upload_to='seguros/images/',
        blank=True, null=True
    )
    min_value_prima = models.IntegerField(
        'Valor mínimo de la prima',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'   


    def __str__(self):
        return '{} ({})'.format(self.name, self.category.name)


class Metadata(models.Model):
    """Guarda la lista de campos necesarios para cada seguro
    """

    TEXT = 'text'
    NUMBER = 'number'
    BOOLEAN = 'checkbox'
    IMAGE = 'image'
    SELECT = 'select'

    TYPES = (
        (TEXT, 'Texto'),
        (NUMBER, 'Numerico'),
        (BOOLEAN, 'Booleano'),
        (IMAGE, 'Imagen'),
        (SELECT, 'Seleccion')
    )


    insurance = models.ForeignKey(
        Insurance, 
        verbose_name="Seguro",
        on_delete=models.CASCADE,
        related_name='related_metadata'
    )
    name = models.CharField(
        'Nombre del campo',
        max_length=255
    )
    field_type = models.CharField(
        'Tipo del campo',
        max_length=10,
        choices=TYPES
    )
    is_required = models.BooleanField(
        'Es requerido?',
        default=True
    )

    class Meta:
        verbose_name = 'Campo del seguro'
        verbose_name_plural = 'Campos de los seguros'


    def __str__(self):
        return '{} del seguro {}'.format(self.name, self.insurance.name)


class MetadataChoices(models.Model):
    """Opciones de cada pregunta cuando es de tipo seleccion
    """

    field = models.ForeignKey(
        Metadata, 
        on_delete=models.CASCADE,
        verbose_name="Campo",
        related_name="related_choices"
    )
    value = models.CharField("Valor", max_length=255)


    class Meta:
        verbose_name = "Opcion del campo"
        verbose_name_plural = "Opciones del campo"

    def __str__(self):
        return "%s" % (self.value)


class InsuranceCoverage(models.Model):
    """Clase para guardar las coverturas de un seguro
    """

    insurance = models.ForeignKey(
        Insurance,
        verbose_name="Seguro",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        "Nombre de la covertura",
        max_length=255
    )
    min_value = models.IntegerField(
        "Valor mínimo de la cobertura",
        blank=True, null=True
    )
    is_required = models.BooleanField(
        "Es requerido?",
        default=False
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Cobertura del seguro'
        verbose_name_plural = 'Coberturas del seguro'


class Insurer(models.Model):
    """Almacena las aseguradoras
    """
    
    insurances = models.ManyToManyField(
        Insurance,
        verbose_name='Seguros',

    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Corredores',
    )
    name = models.CharField(
        'Nombre',
        max_length=50
    )
    cellphone_number = models.CharField(
        'Numero de celular de asistencia',
        max_length=13
    )
    national_number = models.CharField(
        'Linea nacional de asistencia (018000...)',
        max_length=13
    )
    email = models.EmailField(
        'Correo electronico'
    )
    is_active= models.BooleanField(default=True)
    
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
        help_text='Seguro',
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
        related_name='related_insurances_broker',
        blank=True, 
        null=True
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
    request_code = models.CharField(
        'Codigo de la referencia',
        max_length=255,
        blank=True, null=True
    )
    payment_proof = models.ImageField(
        'Recibo de pago SOAT (si aplica)',
        upload_to='Solicitudes/SOAT/recibos',
        blank=True, null=True
    )
    price = models.CharField(
        'Precio del seguro SOAT (Si aplica)',
        max_length=20,
        blank=True, null=True
    )

    def __str__(self):
        return "Solicitud del cliente %s" % (self.client)

    def save(self, *args, **kwargs):
        "Funcion para generar el request_code de la solicitud"

        super(InsuranceRequest, self).save(*args, **kwargs)
        try:
            d = self.request_date
            self.request_code = '{}{}{}{}'.format(d.month, d.day, self.client.pk, self.pk)
        except:
            pass
        super(InsuranceRequest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Historial solicitud'
        verbose_name_plural = 'Historial solicitudes'


class DomiRequestInsurer(models.Model):
    """Guarda los datos del domicilio del cliente que requiere
    que le recogan el dinero del seguro a domicilio
    """

    request_insurance = models.ForeignKey(
        InsuranceRequest,
        verbose_name='Solicitud del seguro',
        on_delete=models.CASCADE
    )
    address = models.CharField(
        'Direccion de recogida',
        max_length=255
    )
    pickup_date = models.DateField(
        'Dia de recogida',
        auto_now=False,
        auto_now_add=False
    )
    pickup_time = models.TimeField(
        'Hora de recogida',
        auto_now_add=False
    )
    contact_phone = models.CharField(
        'Número de contacto',
        max_length=255
    )

    def __str__(self):
        return 'Solicitud de domicilio'
    

    class Meta:
        verbose_name = 'Solicitud de Domicilio'
        verbose_name_plural = 'Solicitudes de Domicilio'


class Answer(models.Model):
    """Guarda las respuestas del formulario de un paciente
    """

    insurance_request = models.ForeignKey(
        InsuranceRequest, 
        verbose_name="Solicitud",
        on_delete=models.CASCADE)
    field = models.ForeignKey(
        Metadata, 
        verbose_name="Campo",
        on_delete=models.CASCADE
    )
    value = models.TextField(
        verbose_name="Respueta",
        help_text='Esta respuesta puede ser de texto abierto, un numero, un booleano,\
            o un id de una respuesta')
    choice = models.CharField("Id de la respuesta", max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        unique_together = ("insurance_request", "field")
    

    def __str__(self):
        return "%s" % (self.value)


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
    """Almacena las polizas que cargan los corredores
    para cada uno de sus clientes
    """

    insurance_request = models.OneToOneField(
        InsuranceRequest,
        on_delete=models.CASCADE,
        verbose_name='Póliza del cliente',
        blank=True, null=True
    )
    insurance = models.ForeignKey(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Seguro',
        verbose_name='Seguro',
        blank=True, null=True
    )
    client = models.ForeignKey(
        get_user_model(),
        verbose_name='Usuario',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        help_text='Enlace a la aseguradora',
        verbose_name='Aseguradora'
    )
    adviser_mail = models.EmailField(
        'Correo asesor',
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    adviser_cellphone = models.CharField(
        'Celular asesor',
        max_length=255,
        blank=True,
        help_text='Agregar en caso de que aplique'
    )
    police_number = models.CharField(
        'Número de póliza - referencia',
        max_length=255,
        blank=True, null=True
    )
    insurance_file = models.FileField(
        'Documento del seguro',
        upload_to = 'Polizas',
        blank=True, null=True
    ) 
    licensed_plate =models.CharField(
        'placa',
        max_length=8,
        default='###-###',
        blank=True, null=True
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
        try:
            return "Póliza %s del cliente %s" % (self.insurance_request.insurance, self.insurance_request.client)
        except:
            return "Póliza del cliente %s" % (self.client)

    
    def clean(self, *args, **kwargs):
        " Funcion para hacer que la fecha de inicio no sea hoy ni menor a hoy "
        d = self.effective_date
        dt = datetime(d.year, d.month, d.day)
        if dt <= datetime.now():
            raise ValidationError('La fecha de inicio de la vigencia debe ser mayor a hoy')
        else:
            self.expiration_date = self.effective_date + relativedelta(years=1) - timezone.timedelta(days=1)
            print (self.expiration_date)
            super(UserPolicy, self).save(*args, **kwargs)
