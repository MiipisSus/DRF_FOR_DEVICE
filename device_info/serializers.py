from rest_framework import serializers

from .models import DeviceBasicInfo, DeviceVideoInfo, DeviceImageInfo

class DeviceBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceBasicInfo
        fields = [
            'device_name',
            'device_location',
            'mac_address',
            'system_boot_time',
            'product_model',
            'firmware_version'
        ]
        
    def update(self, instance: DeviceBasicInfo, validated_data):
        for field, value in validated_data.items():
            if value is not None:
                setattr(instance, field, value)
        
        instance.save()
        return instance
    

class DeviceVideoInfoSerializer(serializers.ModelSerializer):
    profile_0 = serializers.SerializerMethodField()
    profile_1 = serializers.SerializerMethodField()
    profile_2 = serializers.SerializerMethodField()
    
    class Meta:
        model = DeviceBasicInfo
        fields = [
            'profile_0', 
            'profile_1', 
            'profile_2'
        ]
        
    def get_profile_0(self, obj):
        return self.get_profile_data(obj, 'main')
    
    def get_profile_1(self, obj):
        return self.get_profile_data(obj, 'sub')
        
    def get_profile_2(self, obj):
        return self.get_profile_data(obj, 'third')
    
    def update(self, instance: DeviceVideoInfo, validated_data):
        # Bug: The data cannot be received correctly.
        # Try Change to use the parent Serialzier instead of ModelSerializer, should fix it.
        print(validated_data)
        profiles = {
            "profile_0": "main", 
            "profile_1": "sub",
            "profile_2": "third"
            }
        value_fields = ['bit_rate', 'quality', 'jpeg_quality', 'gop']
        for index, info in validated_data.items():
            profile_type = profiles[index]
            for field, value in info.items():
                if field == 'resolution':
                    if value.get('width') is not None:
                        setattr(instance, f'resolution_width_{profile_type}', value.get('width'))
                    if value.get('height') is not None:
                        setattr(instance, f'resolution_height_{profile_type}', value.get('height'))
                elif field in value_fields:
                    setattr(instance, f'{field}_{profile_type}', value.get('value'))
                else:
                    setattr(instance, f'{field}_{profile_type}', value)
        
        instance.save()
        return instance
    
    def get_profile_data(self, obj: DeviceVideoInfo, profile_type):
        return \
        {
            "enabled": getattr(obj, f'enabled_{profile_type}'),
            "encode_type": getattr(obj, f'encode_type_{profile_type}'),
            "bit_rate": 
                {
                    "max": obj._meta.get_field(f'bit_rate_{profile_type}').validators[1].limit_value,
                    "min": obj._meta.get_field(f'bit_rate_{profile_type}').validators[0].limit_value,
                    "value": getattr(obj, f'bit_rate_{profile_type}'),
                    "mode": getattr(obj, f"video_encoding_{profile_type}")
                },
            "quality":
                {
                    "max": obj._meta.get_field(f'quality_{profile_type}').validators[1].limit_value,
                    "min": obj._meta.get_field(f'quality_{profile_type}').validators[0].limit_value,
                    "value": getattr(obj, f'quality_{profile_type}')
                },
            "url": getattr(obj, f'url_{profile_type}'),
            "jpeg_quality":
                {
                    "max": obj._meta.get_field(f'jpeg_quality_{profile_type}').validators[1].limit_value,
                    "min": obj._meta.get_field(f'jpeg_quality_{profile_type}').validators[0].limit_value,
                    "value": getattr(obj, f'jpeg_quality_{profile_type}')
                },
            "gop":
                {
                    "max": obj._meta.get_field(f'gop_{profile_type}').validators[1].limit_value,
                    "min": obj._meta.get_field(f'gop_{profile_type}').validators[0].limit_value,
                    "value": getattr(obj, f'gop_{profile_type}')
                },
            "resolution":
                {
                    "width": getattr(obj, f'resolution_width_{profile_type}'),
                    "height": getattr(obj, f'resolution_height_{profile_type}')
                },
            "frame_rate":
                {
                    "max": obj._meta.get_field(f'frame_rate_{profile_type}').validators[1].limit_value,
                    "min": obj._meta.get_field(f'frame_rate_{profile_type}').validators[0].limit_value,
                    "value": getattr(obj, f'frame_rate_{profile_type}')
                }
        }