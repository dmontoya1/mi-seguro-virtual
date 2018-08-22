# Generated by Django 2.0 on 2018-08-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0013_auto_20180817_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinsurance',
            name='insurance',
        ),
        migrations.AlterModelOptions(
            name='customerpolicy',
            options={'verbose_name': 'Póliza cliente', 'verbose_name_plural': 'Póliza clientes'},
        ),
        migrations.AlterModelOptions(
            name='historyrequestinsurance',
            options={'verbose_name': 'Historial solicitud', 'verbose_name_plural': 'Historial solicitudes'},
        ),
        migrations.AlterModelOptions(
            name='insurance',
            options={'verbose_name': 'Seguro', 'verbose_name_plural': 'Seguros'},
        ),
        migrations.AlterModelOptions(
            name='insurer',
            options={'verbose_name': 'Aseguradora', 'verbose_name_plural': 'Aseguradoras'},
        ),
        migrations.AlterField(
            model_name='customerpolicy',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Imagen'),
        ),
        migrations.DeleteModel(
            name='CustomerInsurance',
        ),
    ]
