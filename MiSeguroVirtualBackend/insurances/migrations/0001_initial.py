# Generated by Django 2.0 on 2018-08-14 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryInsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categoria Seguros',
                'verbose_name': 'Categoria Seguro',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='insurances.CategoryInsurance')),
            ],
            options={
                'verbose_name_plural': 'Seguros',
                'verbose_name': 'Seguro',
            },
        ),
        migrations.CreateModel(
            name='InsuranceDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('insurance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='insurances.Insurance')),
            ],
            options={
                'verbose_name_plural': 'Documento Seguros',
                'verbose_name': 'Documento Seguro',
            },
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cellphone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurances.Insurance')),
            ],
            options={
                'verbose_name_plural': 'Aseguradoras',
                'verbose_name': 'Aseguradora',
            },
        ),
    ]
