# Generated by Django 2.0.6 on 2019-03-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='benefits', verbose_name='Imagen')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('reddeming_code', models.CharField(blank=True, max_length=30, null=True, verbose_name='Codigo para redimir')),
            ],
            options={
                'verbose_name': 'Beneficio',
            },
        ),
    ]
