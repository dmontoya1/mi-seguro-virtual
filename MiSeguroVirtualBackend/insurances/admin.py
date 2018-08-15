from django.contrib import admin
from .models import *


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone', 'email', 'insurance']


@admin.register(InsuranceDocument)
class InsuranceDocumentAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'name']


@admin.register(CategoryInsurance)
class CategoryInsuranceAdmin(admin.ModelAdmin):
    list_display = ['name']
