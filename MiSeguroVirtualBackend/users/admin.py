# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin as django_user_admin
from django.contrib.auth.forms import UserChangeForm as django_change_form
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import User


from .models import (
    User,
    TermsAcceptanceLogs
)

class UserChangeForm(django_change_form):
    class Meta(django_change_form.Meta):
        model = User


class UserAdmin(django_user_admin):
    """Administrador de Usuarios
    """

    form = UserChangeForm
    model = User
    search_fields = (
        'first_name', 'last_name', 'email', 'cellphone', 'document_id'
    )
    list_display = (
        'document_id', 'username','first_name', 'last_name', 'user_type'
    )

    fieldsets = (
        (None,
         {'fields':
          ('username', 'password', 'user_type')}),
        (_('Información Personal'), {'fields': ('first_name', 'last_name', 'email', 'document_type',
                                                'document_id', 'phone_number')}),
        (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups')}),
        (_('Información Bancaria'),
         {'fields': ('bank', 'account_type', 'account_number', 'code')})

    )

    class Media:
        js = (
            'js/admin/utils_admin.js',
        )

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django.
        """
        query = super(UserAdmin, self).get_queryset(request)
        return query.all().exclude(is_superuser=True)
 

@admin.register(TermsAcceptanceLogs)
class TermsAcceptanceLogsAdmin(admin.ModelAdmin):
    list_display = ['ip_address']


admin.site.register(User, UserAdmin)
