# Generated by Django 2.0.6 on 2018-11-09 03:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('CO', 'Corredor de Seguros'), ('IN', 'Influenciador'), ('CL', 'Cliente')], max_length=2, verbose_name='Tipo de usuario')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Número de celular')),
                ('logo', models.ImageField(blank=True, upload_to='logotipos', verbose_name='Imagen')),
                ('document_type', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('CE', 'Cédula de extrajería')], help_text='Tipo de documento de identidad', max_length=20, verbose_name='Tipo de documento')),
                ('document_id', models.CharField(max_length=15, verbose_name='Numero de documento')),
                ('bank', models.CharField(blank=True, max_length=255, null=True, verbose_name='Banco')),
                ('account_type', models.CharField(blank=True, choices=[('AH', 'Ahorros'), ('CO', 'Corriente')], max_length=2, null=True, verbose_name='Tipo de cuenta bancaria')),
                ('account_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de cuenta bancaria')),
                ('code', models.CharField(blank=True, max_length=15, null=True, verbose_name='Código de influencer')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TermsAcceptanceLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acceptance_date', models.DateField(auto_now_add=True, verbose_name='Fecha de solicitud')),
                ('ip_address', models.CharField(max_length=20, verbose_name='IP de aceptacion del cliente')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Log de Términos',
                'verbose_name_plural': 'Logs de términos',
            },
        ),
    ]
