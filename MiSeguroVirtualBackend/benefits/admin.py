from django.contrib import admin


from .models import Benefits


@admin.register(Benefits)
class BenefitsAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', )
    search_fields = ('name', 'reddeming_code')
