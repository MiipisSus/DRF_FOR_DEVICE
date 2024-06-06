from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class StorageInfo(models.Model):
    class FileTypeChoices(models.IntegerChoices):
        jpg = 0
        avi = 1
    
    storage_enabled = models.BooleanField(default=True)
    total_size = models.IntegerField(null=True, default=None)
    used_size = models.IntegerField(null=True, default=None)
    disk_status = models.BooleanField(default=False)
    duration = models.IntegerField(default=60, validators=[MinValueValidator(60), MaxValueValidator(300)])
    record_file_type = models.IntegerField(default=FileTypeChoices.avi)

class File(models.Model):
    class FileTypeChoices(models.IntegerChoices):
        jpg = 0
        avi = 1
        
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(null=True, default=None)
    file_type = models.IntegerField(null=True, default=None, choices=FileTypeChoices.choices)
    file_path = models.CharField(null=True, default=None, max_length=1000)