# Generated by Django 2.0.8 on 2018-08-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0005_auto_20180820_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]