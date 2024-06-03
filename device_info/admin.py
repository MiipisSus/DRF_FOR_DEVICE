from django.contrib import admin
from .models import DeviceInfo, DeviceBasicInfo, DeviceNetworkInfo, DeviceVideoInfo, DeviceImageInfo

# Register your models here.
admin.site.register(DeviceInfo)
admin.site.register(DeviceBasicInfo)
admin.site.register(DeviceNetworkInfo)
admin.site.register(DeviceVideoInfo)
admin.site.register(DeviceImageInfo)