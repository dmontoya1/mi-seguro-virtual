from django.db import models
from django.contrib.auth.models import User


class Broker(models.Model):
    """stores brokers for insures
    """

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=13)

    class Meta:
        verbose_name = 'Corredor'
        verbose_name_plural = 'Corredores'
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    """strores customers of app
    """

    User=models.OneToOneField(User, on_delete=models.CASCADE)
    cellphone = models.CharField(max_length=13)
    document_type = models.CharField(max_length=20)
    document_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def get_full_name(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name

    
    def get_short_name(self):
        return self.User.first_name

    def __str__(self):
        return self.document_number