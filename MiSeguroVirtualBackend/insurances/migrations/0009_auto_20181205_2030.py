# Generated by Django 2.0.6 on 2018-12-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0008_auto_20181127_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurer',
            name='national_number',
            field=models.CharField(default='018000', max_length=13, verbose_name='Linea nacional de asistencia (018000...)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpolicy',
            name='police_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Número de póliza - referencia'),
        ),
        migrations.AddField(
            model_name='userpolicy',
            name='taker_document',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Documento de identidad del tomador'),
        ),
        migrations.AddField(
            model_name='userpolicy',
            name='taker_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre del tomador'),
        ),
        migrations.AlterField(
            model_name='insurer',
            name='cellphone_number',
            field=models.CharField(max_length=13, verbose_name='Numero de celular de asistencia'),
        ),
    ]
