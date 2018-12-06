from django import forms
from django.contrib import admin
from django.db.models import Q
from django.http import HttpResponseRedirect


from .models import (
    Category,
    Subcategory,
    Insurance,
    Metadata,
    MetadataChoices,
    InsuranceCoverage,
    Insurer,
    PointOfSale,
    InsuranceRequest,
    Answer,
    DocumentsRequest,
    UserPolicy
)


class SubcategoryAdmin(admin.TabularInline):

    model = Subcategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']
    inlines = [SubcategoryAdmin, ]


class MetadataChoicesAdmin(admin.StackedInline):
    
    model = MetadataChoices
    extra = 0


@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):

    list_display = ['name', 'field_type', 'is_required']
    inlines = [MetadataChoicesAdmin, ]


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = ["is_active"]


class InsuranceCoverageAdmin(admin.StackedInline):

    model = InsuranceCoverage
    extra = 0


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):

    list_display = ['name', 'category','is_active']
    form = InsuranceForm
    change_form_template = "insurer_changeform.html"
    inlines = [InsuranceCoverageAdmin, ]

    def response_change(self, request, obj):
        if "_enable" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.is_active = True
            obj.save()
            self.message_user(request, "Seguro activado")
            return HttpResponseRedirect(".")
        elif '_disable' in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.is_active = False
            obj.save()
            self.message_user(request, "Seguro desactivado")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


class InsurerForm(forms.ModelForm):
    class Meta:
        model = Insurer
        exclude = ["is_active"]


@admin.register(Insurer)
class InsurerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellphone_number', 'email','is_active']
    form = InsurerForm
    change_form_template = "insurer_changeform.html"

    def response_change(self, request, obj):
        if "_enable" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.is_active = True
            obj.save()
            self.message_user(request, "Aseguradora activada")
            return HttpResponseRedirect(".")
        elif '_disable' in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.is_active = False
            obj.save()
            self.message_user(request, "Aseguradora desactivada")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


class UserPolicyStackAdmin(admin.StackedInline):

    model = UserPolicy
    extra = 0
    readonly_fields = ["expiration_date", ]
    exclude = ('client', 'insurance', )


class DocumentsRequestAdmin(admin.StackedInline):
    
    model = DocumentsRequest
    extra = 0


@admin.register(PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'cellphone_number', 'code']


@admin.register(InsuranceRequest)
class InsuranceRequestAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'client', 'status', 'request_date']
    inlines = [DocumentsRequestAdmin, UserPolicyStackAdmin]

    readonly_fields = [
        'request_code', 
        'insurance', 
        'client', 
        'request_date',
        'price'
    ]

    class Media:
        js = (
            'js/admin/user_request_admin.js',
        )


@admin.register(UserPolicy)
class UserPolicyAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('insurer', 'client', 'effective_date', 'expiration_date')
    exclude = ('insurance_request',)
    readonly_fields = ["expiration_date", ]

    def get_queryset(self, request):
        """
        Función para reemplazar el queryset por defecto de django
        Muestra las polizas que no tienen una solicitud asociada
        """
        query = super(UserPolicyAdmin, self).get_queryset(request)
        return query.filter(insurance_request=None)

    class Media:
        js = (
            'js/admin/user_policy.js',
        )

