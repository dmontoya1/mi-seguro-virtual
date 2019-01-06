from django.apps import AppConfig


class InsurancesConfig(AppConfig):
    name = 'insurances'
    verbose_name = 'Seguros'

    def ready(self):
        import insurances.signals
