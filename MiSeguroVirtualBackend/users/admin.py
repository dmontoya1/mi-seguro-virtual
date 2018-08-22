from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django import forms

from users.forms import UserChangeForm, UserCreationForm

from .models import (
    Broker,
    Customer
)

User = get_user_model()


class BrokerForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = Broker
        exclude = ["user"]

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    form = BrokerForm

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



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cellphone_number']