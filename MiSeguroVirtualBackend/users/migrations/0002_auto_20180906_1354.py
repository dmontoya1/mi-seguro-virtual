# Generated by Django 2.0.6 on 2018-09-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='document_type',
            field=models.CharField(choices=[('CC', 'Cedula'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte'), ('CE', 'Cedula de extrajeria')], help_text='Tipo de documento de identidad', max_length=20, verbose_name='Tipo de documento'),
        ),
    ]
