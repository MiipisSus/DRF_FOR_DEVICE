# Generated by Django 4.0.10 on 2024-06-04 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0005_deviceimageinfo_night_mode_exposure_enabled_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deviceimageinfo',
            old_name='day_exposure_Gain',
            new_name='day_exposure_gain',
        ),
    ]
