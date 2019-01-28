# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authtoken.models import Token

from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template import Template, Context, loader
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from users.models import User, TermsAcceptanceLogs


class HomePageView(TemplateView):

    template_name = "webclient/home.html"



class TestView(TemplateView):

    template_name = "webclient/test.html"


class PoliciesView(TemplateView):

    template_name = "webclient/policies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _type = self.kwargs.get('type', 'PP')
        if _type:
            if self.kwargs['type'] == 'privacy':
                _type = 'PP'
            elif self.kwargs['type'] == 'terms':
                _type = 'TCP'
            elif self.kwargs['type'] == 'cookies':
                _type = 'CMP'
        police = get_object_or_404(Policy, policy_type=_type)
        context = super(PoliciesView, self).get_context_data(**kwargs)
        context['name'] = police.get_policy_type_display()
        context['content'] = police.content
        return context



class LoginView(TemplateView):
    """Iniciar Sesión
    """

    template_name = "webclient/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, user_type=User.INFLUENCER)
        except User.DoesNotExist:
            response = {'error': 'El correo no se encuentra registrado en la plataforma como influencer'}
            return JsonResponse(response, status=400)
        user = authenticate(username=username, password=password)
        if user is not None:
            url = reverse('webclient:profile')
            login(request, user)
            messages.add_message(
                request,
                messages.ERROR, 
                "Hola influencer"
            )
        else:
            response = {'error': 'Correo y/o contraseña incorrectas.'}
            return JsonResponse(response, status=400)

        return JsonResponse(url, safe=False)


class SignupView(TemplateView):
    """Clase para Registrar un usuario
    """

    template_name = "webclient/signup.html"


    def post(self, request, *args, **kwargs):
        try:
            user = User()
            username = request.POST['email']
            password = request.POST['password1']
            user.email = username
            user.username = username
            user.set_password(password)
            user.user_type = User.INFLUENCER
            user.code = get_random_string(length=10)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            user = authenticate(username=username, password=password)

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
				
            log = TermsAcceptanceLogs(
                ip_address=ip,
                user=user
            )
            log.save()

            messages.add_message(
                request,
                messages.ERROR, 
                "Te has registrado correctamente. Actualiza tu perfil para disfrutar de las ventajas de ser un Influencer"
            )
            url = reverse('webclient:profile')
            return JsonResponse(url, safe=False)
        except IntegrityError:
            msg = 'Tu correo ya está registrado. Por favor inicia sesión'
            response = {'error': msg}
            return JsonResponse(response, status=400)


class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = "webclient/profile.html"
    login_url = 'webclient:login'


class InfluencerProfits(LoginRequiredMixin, TemplateView):
    """
    """

    template_name = "webclient/influencer_profits.html"
    login_url = "webclient:login"
