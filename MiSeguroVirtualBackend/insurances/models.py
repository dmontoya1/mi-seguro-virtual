from django.db import models


class CategoryInsurance(models.Model):
    """stores diferent categories for insurences
    """

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria Seguro'
        verbose_name_plural = 'Categoria Seguros'
    
    def __str__(self):
        return self.name


class Insurance(models.Model):
    """store insurence for document insurance
    """

    name = models.CharField(max_length=50)
    category = models.OneToOneField(CategoryInsurance, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'
    
    def __str__(self):
        return self.name


class Insurer(models.Model):
    """stores companies insures
    """

    name = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=13)
    email = models.EmailField()
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aseguradora'
        verbose_name_plural = 'Aseguradoras'
    
    def __str__(str):
        return self.name


class InsuranceDocument(models.Model):
    """stores documents insurances for costumers of app
    """

    insurance = models.OneToOneField(Insurance, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Documento Seguro'
        verbose_name_plural = 'Documento Seguros'

    def __str__(self):
        return self.name