# Generated by Django 2.0.6 on 2018-09-11 19:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180906_1354'),
        ('insurances', '0007_auto_20180910_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpolicy',
            name='licensed_plate',
            field=models.CharField(default='###-###', max_length=8, verbose_name='placa'),
        ),
        migrations.AddField(
            model_name='insurancerequest',
            name='adviser_code',
            field=models.CharField(blank=True, help_text='Agregar en caso de que aplique', max_length=15, verbose_name='Codigo asesor'),
        ),
        migrations.AddField(
            model_name='insurancerequest',
            name='broker',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Broker', verbose_name='Corredores'),
        ),
        migrations.AlterField(
            model_name='customerpolicy',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 12, 19, 49, 32, 618571, tzinfo=utc), verbose_name='Fecha de vencimiento'),
        ),
    ]