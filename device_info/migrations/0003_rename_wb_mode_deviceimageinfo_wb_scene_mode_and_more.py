# Generated by Django 4.0.10 on 2024-06-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0002_devicevideoinfo_enabled_main_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deviceimageinfo',
            old_name='wb_mode',
            new_name='wb_scene_mode',
        ),
        migrations.AddField(
            model_name='deviceimageinfo',
            name='wb_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='deviceimageinfo',
            name='wb_scene_value',
            field=models.IntegerField(default=0),
        ),
    ]