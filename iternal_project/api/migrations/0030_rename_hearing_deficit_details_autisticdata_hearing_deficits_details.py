# Generated by Django 4.0.4 on 2022-08-04 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_rename_concerns_first_noticed_in_autisticdata_impression_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autisticdata',
            old_name='hearing_deficit_details',
            new_name='hearing_deficits_details',
        ),
    ]
