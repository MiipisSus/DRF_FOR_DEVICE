# Generated by Django 4.0.10 on 2024-06-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0003_rename_wb_mode_deviceimageinfo_wb_scene_mode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceimageinfo',
            name='exposure_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
