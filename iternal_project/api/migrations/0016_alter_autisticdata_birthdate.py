# Generated by Django 4.0.4 on 2022-07-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_autisticdata_speechdevdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autisticdata',
            name='birthDate',
            field=models.CharField(default='', max_length=20),
        ),
    ]
