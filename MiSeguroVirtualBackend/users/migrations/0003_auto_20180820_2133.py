# Generated by Django 2.0.8 on 2018-08-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_broker_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='insurances',
            field=models.ManyToManyField(blank=True, null=True, to='insurances.Insurance', verbose_name='Seguros'),
        ),
    ]