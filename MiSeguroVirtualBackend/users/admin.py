from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django import forms
from django.http import HttpResponseRedirect

from users.forms import UserChangeForm, UserCreationForm

from .models import (
    Broker,
    Customer,
    TermsAcceptanceLogs
)

User = get_user_model()


class BrokerForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = Broker
        exclude = ["user", "active"]

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ['user','active']
    form = BrokerForm
    change_form_template = "insurer_changeform.html"

    def save_model(self, request, obj, form, change):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user, created = User.objects.get_or_create(username=email)
        user.set_password(password)
        user.email = email
        user.is_staff = True
        user.save()
        group = Group.objects.get(name='Brokers')
        group.user_set.add(user)
        obj.user = user
        super().save_model(request, obj, form, change)
    
    def response_change(self, request, obj):
        if "_enable" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = True
            obj.save()
            self.message_user(request, "Corredor activado")
            return HttpResponseRedirect(".")
        elif '_disable' in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.active = False
            obj.save()
            self.message_user(request, "Corredor desactivado")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(TermsAcceptanceLogs)
class TermsAcceptanceLogsAdmin(admin.ModelAdmin):
    list_display = ['ip_address']