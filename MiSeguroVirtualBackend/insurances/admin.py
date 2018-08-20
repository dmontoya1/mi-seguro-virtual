from django import forms
from django.contrib import admin
from django.http import HttpResponseRedirect

from admin_view_permission.admin import AdminViewPermissionAdminSite

from .models import (
    AuthorizedPoint,
    CustomerPolicy,
    HistoryRequestInsurance,
    Insurance,
    InsuranceCategory,
    Insurer
)



@admin.register(AuthorizedPoint)
class AuthorizedPointAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerPolicy)
class CustomerPolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(HistoryRequestInsurance)
class HistoryRequestInsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(InsuranceCategory)
class InsuranceCategoryAdmin(admin.ModelAdmin):
    pass


class InsurerForm(forms.ModelForm):
    class Meta:
        model = Insurer
        exclude = ["active"]

@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    form = InsurerForm
    change_form_template = "admin/insurer/insurer_changeform.html"

    def response_change(self, request, obj):
        if "_enable" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = True
            obj.save()
            self.message_user(request, "Insurer Activated")
            return HttpResponseRedirect(".")
        elif '_disable' in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = False
            obj.save()
            self.message_user(request, "Insurer Deactivated")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)