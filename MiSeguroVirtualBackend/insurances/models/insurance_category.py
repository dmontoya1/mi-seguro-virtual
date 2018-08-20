from django.db import models


class InsuranceCategory(models.Model):
    """
        Almacena las categorias que tendran los seguros
        Save the categories that include all insurances
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

