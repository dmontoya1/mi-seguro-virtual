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


class Insurance(models.Model):
    """almacena los seguros para la venta
    """

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


class Insurer(models.Model):
    """almacena las aseguradoras
    """

    insurance = models.ForeignKey(
        Insurance,
        on_delete=models.CASCADE,
        help_text='Enlace a los seguros',
        verbose_name='Seguros'
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
    
    def __str__(self):
        return self.name


class InsuranceDocument(models.Model):
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
        verbose_name = 'Documento Seguro'
        verbose_name_plural = 'Documento Seguros'

    def __str__(self):
        return self.name