# Generated by Django 2.0.6 on 2019-01-06 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0016_userpolicy_old_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentsrequest',
            name='drive_license',
        ),
        migrations.RemoveField(
            model_name='documentsrequest',
            name='property_card',
        ),
        migrations.AddField(
            model_name='documentsrequest',
            name='old_soat',
            field=models.ImageField(blank=True, upload_to='Solicitudes/licencias', verbose_name='Soat Anterior'),
        ),
        migrations.AddField(
            model_name='documentsrequest',
            name='property_card_back',
            field=models.ImageField(blank=True, upload_to='Solicitudes/tarjetas', verbose_name='Tarjeta de propiedad atras'),
        ),
        migrations.AddField(
            model_name='documentsrequest',
            name='property_card_front',
            field=models.ImageField(blank=True, upload_to='Solicitudes/tarjetas', verbose_name='Tarjeta de propiedad frente'),
        ),
    ]