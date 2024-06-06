from rest_framework import serializers

from .models import *

class DeviceBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceBasicInfo
        fields = '__all__'
        
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if value is not None:
                setattr(instance, field, value)
        
        instance.save()
        return instance
    

class DeviceNetworkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceNetworkInfo
        fields = '__all__'
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if value is not None:
                setattr(instance, field, value)
        
        instance.save()
        return instance
    
    
class DeviceOSDInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceOSDInfo
        fields = '__all__'
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if value is not None:
                setattr(instance, field, value)
        
        instance.save()
        return instance


class DeviceVideoInfoSerializer(serializers.ModelSerializer):
    profile_0 = serializers.JSONField()
    profile_1 = serializers.JSONField()
    profile_2 = serializers.JSONField()

    class Meta:
        model = DeviceVideoInfo
        fields = [
            'profile_0', 
            'profile_1', 
            'profile_2'
        ]
        
    def to_representation(self, instance):
        return {
            'profile_0': self.get_profile_data(instance, 'main'),
            'profile_1': self.get_profile_data(instance, 'sub'),
            'profile_2': self.get_profile_data(instance, 'third')
        }
    
    def update(self, instance: DeviceVideoInfo, validated_data):
        '''
        --------------------------
        Field structure (per profile_info)
        
        enabled
        encode_type
        bitrate -> max, min, value, mode
        quality -> max, min, value
        url
        jpeg_quality -> max, min, value
        gop -> max, min, value
        resolution -> width, height
        frame_rate -> max, min, value
        --------------------------
        '''
        profiles = {
            "profile_0": "main", 
            "profile_1": "sub",
            "profile_2": "third"
            }
        nested_fields = ['bit_rate', 'quality', 'jpeg_quality', 'gop', 'frame_rate']
        for index, info in validated_data.items():
            profile_type = profiles[index]
            for field, value in info.items():
                if field == 'resolution':
                    self.set_attributes(instance, value, {'width': f'resolution_width_{profile_type}',
                                                          'height': f'resolution_height_{profile_type}'})
                elif field in nested_fields:
                    self.set_attributes(instance, value, {'value': f'{field}_{profile_type}'})
                else:
                    setattr(instance, f'{field}_{profile_type}', value)
        
        instance.save()
        return instance
    
    def set_attributes(self, instance, value, mapping):
        for key, attribute in mapping.items():
            if key in value:
                setattr(instance, attribute, value[key])
                
    def set_resolution_field(self, instance: DeviceVideoInfo, value, profile_type = 'main'):
        if value.get('width') is not None:
            self.set_attributes(instance, value, {'width': f'resolution_width_{profile_type}'})
            setattr(instance, f'resolution_width_{profile_type}', value.get('width'))
        if value.get('height') is not None:
            setattr(instance, f'resolution_height_{profile_type}', value.get('height'))
    
    def get_profile_data(self, instance: DeviceVideoInfo, profile_type):
        return \
        {
            "enabled": getattr(instance, f'enabled_{profile_type}'),
            "encode_type": getattr(instance, f'encode_type_{profile_type}'),
            "bit_rate": 
                {
                    "max": instance._meta.get_field(f'bit_rate_{profile_type}').validators[1].limit_value,
                    "min": instance._meta.get_field(f'bit_rate_{profile_type}').validators[0].limit_value,
                    "value": getattr(instance, f'bit_rate_{profile_type}'),
                    "mode": getattr(instance, f"video_encoding_{profile_type}")
                },
            "quality":
                {
                    "max": instance._meta.get_field(f'quality_{profile_type}').validators[1].limit_value,
                    "min": instance._meta.get_field(f'quality_{profile_type}').validators[0].limit_value,
                    "value": getattr(instance, f'quality_{profile_type}')
                },
            "url": getattr(instance, f'url_{profile_type}'),
            "jpeg_quality":
                {
                    "max": instance._meta.get_field(f'jpeg_quality_{profile_type}').validators[1].limit_value,
                    "min": instance._meta.get_field(f'jpeg_quality_{profile_type}').validators[0].limit_value,
                    "value": getattr(instance, f'jpeg_quality_{profile_type}')
                },
            "gop":
                {
                    "max": instance._meta.get_field(f'gop_{profile_type}').validators[1].limit_value,
                    "min": instance._meta.get_field(f'gop_{profile_type}').validators[0].limit_value,
                    "value": getattr(instance, f'gop_{profile_type}')
                },
            "resolution":
                {
                    "width": getattr(instance, f'resolution_width_{profile_type}'),
                    "height": getattr(instance, f'resolution_height_{profile_type}')
                },
            "frame_rate":
                {
                    "max": instance._meta.get_field(f'frame_rate_{profile_type}').validators[1].limit_value,
                    "min": instance._meta.get_field(f'frame_rate_{profile_type}').validators[0].limit_value,
                    "value": getattr(instance, f'frame_rate_{profile_type}')
                }
        }
        

class DeviceImageInfoSerializer(serializers.ModelSerializer):
    imaging_0 = serializers.JSONField()
    
    class Meta:
        model = DeviceImageInfo
        fields = [
            'imaging_0'
        ]
        
    def to_representation(self, instance):
        return {
                'imaging_0': self.get_imaging_data(instance)
                }
        
    def update(self, instance: DeviceImageInfo, validated_data):
        '''
        --------------------------
        Field structure
        
        flip
        mirror
        icr -> value, time_start, time_end
        bw_mode
        wb -> enabled, scene_mode, scene_value
        exposure -> enabled, flickness, day_mode (mode, time, gain), night_mode(mode, time, gain)
        brightness -> day_mode (value, max, min), night_mode (value, max, min)
        sharpness -> day_mode (value, max, min), night_mode (value, max, min)
        contrast -> day_mode (value, max, min), night_mode (value, max, min)
        hue -> day_mode (value, max, min), night_mode (value, max, min)
        saturation -> day_mode (value, max, min), night_mode (value, max, min)
        wdr -> day_mode (enabled, value), night_mode (enabled, value)
        --------------------------
        '''
        imaging_data = validated_data.get('imaging_0')
        for field, value in imaging_data.items():
            if field == 'icr':
                self.set_icr_field(instance, value)
            elif field == 'wb':
                self.set_wb_field(instance, value)
            elif field == 'exposure':
                self.set_exposure_field(instance, value)
            elif field in ('brightness', 'sharpness', 'contrast', 'hue', 'saturation', 'wdr'):
                self.set_field_including_day_night(instance, value, field)
            
            instance.save()
            return instance
    
    def set_attributes(self, instance, value, mapping):
        for key, attribute in mapping.items():
            if key in value:
                setattr(instance, attribute, value[key])

    def set_icr_field(self, instance: DeviceImageInfo, value):
        keys_mapping = {
            'value': 'icr',
            'time_start': 'icr_day_mode_start',
            'time_end': 'icr_day_mode_end'
            }
        self.set_attributes(instance, value, keys_mapping)
    
    def set_wb_field(self, instance: DeviceImageInfo, value):
        keys_mapping = {
            'enabled': 'wb_enabled',
            'scene_mode': 'wb_scene_mode',
            'scene_value': 'wb_scene_value'
        }
        self.set_attributes(instance, value, keys_mapping)
            
    def set_exposure_field(self, instance: DeviceImageInfo, value):
        keys_mapping = {
            'enabled': 'exposure_enabled',
            'flickness': 'flickness'
        }
        self.set_attributes(instance, value, keys_mapping)
        
        day_mode = value.get('day_mode')
        if day_mode is not None:
            keys_mapping = {
                'mode': 'day_mode_exposure',
                'time': 'day_exposure_time',
                'gain': 'day_exposure_gain'
            }
            self.set_attributes(instance, day_mode, keys_mapping)
        night_mode = value.get('night_mode')
        if night_mode is not None:
            keys_mapping = {
                'mode': 'night_mode_exposure',
                'time': 'night_exposure_time',
                'gain': 'night_exposure_gain'
            }
            self.set_attributes(instance, night_mode, keys_mapping)
                
    def set_field_including_day_night(self, instance: DeviceImageInfo, value, field):
        day_mode = value.get('day_mode')
        if day_mode is not None and day_mode.get('value') is not None:
            self.set_attributes(instance, day_mode, {'value': field})
        night_mode = value.get('night_mode')
        if night_mode is not None and night_mode.get('value') is not None:
            self.set_attributes(instance, day_mode, {'value': f"{field}_night"})
    
    def get_imaging_data(self, instance: DeviceImageInfo):
        return \
            {
                "flip": instance.flip,
                "mirror": instance.mirror,
                "icr":
                    {
                        "value": instance.icr,
                        "time_start": instance.icr_day_mode_start,
                        "time_end": instance.icr_day_mode_end
                    },
                "bw_mode": instance.bw_mode,
                "wb":
                    {
                        "enabled": instance.wb_enabled,
                        "scene_mode": instance.wb_scene_mode,
                        "scene_value": instance.wb_scene_value
                    },
                "exposure":
                    {
                        "enabled": instance.exposure_enabled,
                        "flickness": instance.flickness,
                        "day_mode":
                            {
                                "mode": instance.day_mode_exposure,
                                "time": instance.day_exposure_time,
                                "gain": instance.day_exposure_gain
                            },
                        "night_mode":
                            {
                                "mode": instance.night_mode_exposure,
                                "time": instance.night_exposure_time,
                                "gain": instance.night_exposure_gain
                            }
                    },
                "brightness": 
                    {
                        "day_mode":
                            {
                                "value": instance.brightness,
                                "max": instance._meta.get_field('brightness').validators[1].limit_value,
                                "min": instance._meta.get_field('brightness').validators[0].limit_value,
                                "default": instance._meta.get_field('brightness').default,
                            },
                        "night_mode":
                            {
                                "value": instance.brightness_night,
                                "max": instance._meta.get_field('brightness_night').validators[1].limit_value,
                                "min": instance._meta.get_field('brightness_night').validators[0].limit_value,
                                "default": instance._meta.get_field('brightness_night').default,
                            }
                    },
                "sharpness": 
                    {
                        "day_mode":
                            {
                                "value": instance.sharpness,
                                "max": instance._meta.get_field('sharpness').validators[1].limit_value,
                                "min": instance._meta.get_field('sharpness').validators[0].limit_value,
                                "default": instance._meta.get_field('sharpness').default,
                            },
                        "night_mode":
                            {
                                "value": instance.sharpness_night,
                                "max": instance._meta.get_field('sharpness_night').validators[1].limit_value,
                                "min": instance._meta.get_field('sharpness_night').validators[0].limit_value,
                                "default": instance._meta.get_field('sharpness_night').default,
                            }
                    },
                "contrast": 
                    {
                        "day_mode":
                            {
                                "value": instance.contrast,
                                "max": instance._meta.get_field('contrast').validators[1].limit_value,
                                "min": instance._meta.get_field('contrast').validators[0].limit_value,
                                "default": instance._meta.get_field('contrast').default,
                            },
                        "night_mode":
                            {
                                "value": instance.contrast_night,
                                "max": instance._meta.get_field('contrast_night').validators[1].limit_value,
                                "min": instance._meta.get_field('contrast_night').validators[0].limit_value,
                                "default": instance._meta.get_field('contrast_night').default,
                            }
                    },
                "hue": 
                    {
                        "day_mode":
                            {
                                "value": instance.hue,
                                "max": instance._meta.get_field('hue').validators[1].limit_value,
                                "min": instance._meta.get_field('hue').validators[0].limit_value,
                                "default": instance._meta.get_field('hue').default,
                            },
                        "night_mode":
                            {
                                "value": instance.hue_night,
                                "max": instance._meta.get_field('hue_night').validators[1].limit_value,
                                "min": instance._meta.get_field('hue_night').validators[0].limit_value,
                                "default": instance._meta.get_field('hue_night').default,
                            }
                    },
                "saturation": 
                    {
                        "day_mode":
                            {
                                "value": instance.saturation,
                                "max": instance._meta.get_field('saturation').validators[1].limit_value,
                                "min": instance._meta.get_field('saturation').validators[0].limit_value,
                                "default": instance._meta.get_field('saturation').default,
                            },
                        "night_mode":
                            {
                                "value": instance.saturation_night,
                                "max": instance._meta.get_field('saturation_night').validators[1].limit_value,
                                "min": instance._meta.get_field('saturation_night').validators[0].limit_value,
                                "default": instance._meta.get_field('saturation_night').default,
                            }
                    },
                "wdr":
                    {
                        "day_mode":
                            {
                                "enabled": instance.wdr_enabled,
                                "value": instance.wdr
                            },
                        "night_mode":
                            {
                                "enabled": instance.wdr_night_enabled,
                                "value": instance.wdr_night
                            }
                    }
            }