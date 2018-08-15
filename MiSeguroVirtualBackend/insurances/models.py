from django.db import models


class CategoryInsurance(models.Model):
    """almacena las categorias que tendran los seguros
    """

    name = models.CharField(
        'Nombre',
        max_length=50
    )

    class Meta:
        verbose_name = 'Categoria Seguro'
        verbose_name_plural = 'Categoria Seguros'
    
    def __str__(self):
        return self.name


class Insurer(models.Model):
    """almacena las aseguradoras
    """

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


class Insurance(models.Model):
    """almacena los seguros para la venta
    """
    insurer = models.ForeignKey(
        Insurer,
        on_delete=models.CASCADE,
        help_text='Enlace a la aseguradora',
        verbose_name='Aseguradora',
        default=None

    )
    category = models.OneToOneField(
        CategoryInsurance,
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


class CustomerInsurance(models.Model):
    """almacena las pólizas creadas
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