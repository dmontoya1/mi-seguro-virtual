from django.db import models


class Benefits(models.Model):
    """

    """

    name = models.CharField(
        'Nombre',
        max_length=255
    )
    image = models.ImageField(
        'Imagen',
        upload_to='benefits'
    )
    description = models.TextField(
        'Descripcion'
    )
    reddeming_code = models.CharField(
        'Codigo para redimir',
        max_length=30,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Beneficio'
