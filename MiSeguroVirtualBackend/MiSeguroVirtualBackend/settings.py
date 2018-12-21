import os
import datetime

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-2a8n5@ut6b#@4!qb^cxap1)%#sk-z0h3u&oed&fzh(6!o$bxv'


DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    'admin_view_permission',
    'rest_framework',
    'rest_framework_swagger',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'fcm_django',
]

PROJECT_APPS = [
    'apis',
    'insurances',
    'notifications',
    'users',
    'webclient'
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MiSeguroVirtualBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'MiSeguroVirtualBackend/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MiSeguroVirtualBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insurances',
    }
}

AUTH_USER_MODEL = 'users.User'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#Email settings sendGrid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_USER = 'Mi Seguro Virtual <no-reply@quality-seguros.com>'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Internationalization
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "MiSeguroVirtualBackend/static")
]

# User uploades files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, "MiSeguroVirtualBackend/media")


AUTH_USER_MODEL = 'users.User'

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'es_CO',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'
        }
    }

#facebook
SOCIAL_AUTH_FACEBOOK_KEY = '1705416796237021'
SOCIAL_AUTH_FACEBOOK_SECRET ='f3fe0a12248ea9b858219b8f5f3a48e7'

LOGIN_REDIRECT_URL = "webclient:profile" 

JWT_AUTH = {

    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=50),

}

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAuu9IJxk:APA91bHiVjxqhfnpnUj24NWEPt7gSQTVCwEiSHWmc1SzhIo7-2FsKAiTa3vp1uErRU62HgRScbRCqnrVki2N0mcHwli4j_Jdn_cdf0WJvNLFoFnpE5zwBR6DjsQoRAfuByw6GwaE_pU5",
        "ONE_DEVICE_PER_USER": True,
        "DELETE_INACTIVE_DEVICES": True,
}