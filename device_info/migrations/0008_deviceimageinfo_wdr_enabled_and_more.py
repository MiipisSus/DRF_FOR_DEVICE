# Generated by Django 4.0.10 on 2024-06-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0007_rename_night_exposure_gain_deviceimageinfo_night_exposure_gain'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceimageinfo',
            name='wdr_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deviceimageinfo',
            name='wdr_night_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
