# Generated by Django 2.0 on 2018-08-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0014_auto_20180822_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
