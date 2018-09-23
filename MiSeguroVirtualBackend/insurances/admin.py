from django import forms
from django.contrib import admin
from django.http import HttpResponseRedirect


from .models import (
    PointOfSale,
    UserPolicy,
    InsuranceRequest,
    Insurance,
    InsuranceCategory,
    Insurer,
    DocumentsRequest
)


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = ["active"]


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','active']
    form = InsuranceForm
    change_form_template = "insurer_changeform.html"

    def response_change(self, request, obj):
        if "_enable" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = True
            obj.save()
            self.message_user(request, "Seguro activado")
            return HttpResponseRedirect(".")
        elif '_disable' in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = False
            obj.save()
            self.message_user(request, "Seguro desactivado")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


class InsurerForm(forms.ModelForm):
    class Meta:
        model = Insurer
        exclude = ["active"]


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone_number', 'email','active']
    form = InsurerForm
    change_form_template = "insurer_changeform.html"

    def response_change(self, request, obj):
        if "_enable" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = True
            obj.save()
            self.message_user(request, "Aseguradora activada")
            return HttpResponseRedirect(".")
        elif '_disable' in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = False
            obj.save()
            self.message_user(request, "Aseguradora desactivada")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)



@admin.register(UserPolicy)
class UserPolicyAdmin(admin.ModelAdmin):
    list_display = ['insurer', 'insurance', 'effective_date']



class DocumentsRequestAdmin(admin.StackedInline):
    
    model = DocumentsRequest
    extra = 0


@admin.register(InsuranceCategory)
class CategoryInsuranceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'cellphone_number', 'code']


@admin.register(InsuranceRequest)
class InsuranceRequestAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'client', 'status', 'request_date']
    inlines = [DocumentsRequestAdmin, ]
