from django.contrib import admin
from .models import *

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cellphone']