# Generated by Django 2.0.6 on 2018-09-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0004_auto_20180929_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpolicy',
            name='image',
        ),
        migrations.AddField(
            model_name='userpolicy',
            name='insurance_file',
            field=models.FileField(blank=True, upload_to='Polizas', verbose_name='Documento del seguro'),
        ),
    ]
