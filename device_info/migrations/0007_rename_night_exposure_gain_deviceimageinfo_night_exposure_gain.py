# Generated by Django 4.0.10 on 2024-06-04 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0006_rename_day_exposure_gain_deviceimageinfo_day_exposure_gain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deviceimageinfo',
            old_name='night_exposure_Gain',
            new_name='night_exposure_gain',
        ),
    ]
