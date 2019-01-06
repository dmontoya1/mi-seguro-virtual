
from django.conf import settings
from django.db import models

# Create your models here.

class Notification(models.Model):
    """
    Modelo para guardar las notificaciones que se envían a los acudientes
    sea desde el administrador, o desde la ruta, o desde donde se necesite
    """

    date = models.DateTimeField("Fecha", auto_now_add=True)
    title = models.CharField("Título", max_length=50)
    description = models.CharField("Descripción", max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name="Usuario",
        blank=True, 
        null=True, 
        related_name='related_user_notification',
        on_delete=models.SET_NULL
    )


    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"
