# Generated by Django 4.0.10 on 2024-06-06 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StorageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage_enabled', models.BooleanField(default=True)),
                ('total_size', models.IntegerField(default=None, null=True)),
                ('used_size', models.IntegerField(default=None, null=True)),
                ('disk_status', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=60, validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(300)])),
                ('record_file_type', models.CharField(default='*.avi', max_length=30)),
            ],
        ),
    ]
