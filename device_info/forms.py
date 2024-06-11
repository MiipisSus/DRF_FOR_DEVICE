from django.forms import ModelForm
from device_info.models import *

class DeviceBasicForm(ModelForm):
    class Meta:
        model = DeviceBasicInfo
        fields = [
            'device_name',
            'device_location'
            ]