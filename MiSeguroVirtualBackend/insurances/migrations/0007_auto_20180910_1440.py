# Generated by Django 2.0.6 on 2018-09-10 19:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180906_1354'),
        ('insurances', '0006_auto_20180909_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpolicy',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.Customer', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='customerpolicy',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 11, 19, 40, 34, 446156, tzinfo=utc), verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='customerpolicy',
            name='effective_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha inicio de vigencia'),
        ),
    ]
