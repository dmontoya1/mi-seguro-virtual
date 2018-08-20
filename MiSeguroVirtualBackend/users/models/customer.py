from django.db import models

from .user import User

class Customer(models.Model):
    """almacena los clientes que desean adquirir seguros
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text='Enlace al usuario',
        verbose_name='Usuario'
    )
    cellphone_number = models.CharField(
        'Número de celular',
        max_length=13
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=20,
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