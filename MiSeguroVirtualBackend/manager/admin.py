# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.db.models import Q
from users.models import User
from .models import Police


@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    """
    Clase para administrar las políticas de la plataforma
    """

    model = Police
    icon = '<i class="material-icons">account_balance</i>'
    search_fields = (
        'name', 'police_type'
    )
    list_display = (
        'name', 'police_type'
    )
    fieldsets = (
        (None, {
            'fields': (
                'police_type', 'name', 'text'
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        messages.set_level(request, messages.WARNING)
        messages.warning(request, 'Política grabada exitosamente')
        super(PoliceAdmin, self).save_model(request, obj, form, change)

