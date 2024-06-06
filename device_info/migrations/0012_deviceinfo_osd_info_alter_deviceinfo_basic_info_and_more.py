# Generated by Django 4.0.10 on 2024-06-06 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device_info', '0011_remove_deviceinfo_osd_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='osd_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device_info.deviceosdsetting'),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='basic_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device_info.devicebasicinfo'),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='image_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device_info.deviceimageinfo'),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='network_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device_info.devicenetworkinfo'),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='video_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='device_info.devicevideoinfo'),
        ),
    ]
