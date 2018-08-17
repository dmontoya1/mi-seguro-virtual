from django.contrib import admin
from .models import *


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone_number', 'email']


@admin.register(CustomerPolicy)
class CustomerPolicyAdmin(admin.ModelAdmin):
    list_display = ['insurer', 'insurance', 'effective_date']


@admin.register(InsuranceCategory)
class CategoryInsuranceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AuthorizedPoint)
class AuthorizedPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'cellphone_number', 'code']


@admin.register(HistoryRequestInsurance)
class HistoryRequestInsuranceAdmin(admin.ModelAdmin):
    pass
