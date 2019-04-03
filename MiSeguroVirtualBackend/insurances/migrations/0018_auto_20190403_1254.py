# Generated by Django 2.0.6 on 2019-04-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0017_auto_20190105_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Solicitudes/imagenes', verbose_name='Imágen'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='value',
            field=models.TextField(blank=True, help_text='Esta respuesta puede ser de texto abierto, un numero, un booleano,            o un id de una respuesta', null=True, verbose_name='Respueta'),
        ),
    ]
