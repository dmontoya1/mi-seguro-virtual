# Generated by Django 2.0.8 on 2018-08-20 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Seguro',
                'verbose_name_plural': 'Seguros',
            },
        ),
        migrations.CreateModel(
            name='InsuranceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria de seguro',
                'verbose_name_plural': 'Categoria de seguros',
            },
        ),
        migrations.AddField(
            model_name='insurance',
            name='category',
            field=models.OneToOneField(help_text='Enlace a la categoria del seguro', on_delete=django.db.models.deletion.CASCADE, to='insurances.InsuranceCategory', verbose_name='Categoria seguro'),
        ),
    ]