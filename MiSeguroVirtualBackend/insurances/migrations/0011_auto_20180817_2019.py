# Generated by Django 2.0 on 2018-08-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0010_customerpolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpolicy',
            name='effective_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de vigencia'),
        ),
    ]
