# Generated by Django 2.0.6 on 2018-11-07 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0007_auto_20181107_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='imagen',
            new_name='image',
        ),
    ]
