# Generated by Django 2.0 on 2018-08-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0016_insurance_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpolicy',
            name='image',
            field=models.ImageField(blank=True, upload_to='Polizas', verbose_name='Imagen'),
        ),
    ]
