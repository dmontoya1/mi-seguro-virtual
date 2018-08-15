from django.contrib import admin
from .models import *


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone_number', 'email']


@admin.register(CustomerInsurance)
class InsuranceDocumentAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'name']


@admin.register(InsuranceCategory)
class CategoryInsuranceAdmin(admin.ModelAdmin):
    list_display = ['name']
