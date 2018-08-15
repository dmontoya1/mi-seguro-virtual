from django.contrib import admin
from .models import *


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone_number']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cellphone_number']