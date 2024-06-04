from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import DeviceVideoInfo, DeviceImageInfo

import json


class GetMultimediaValueVideoView(APIView):
    def get(self, request):
        video_info = DeviceVideoInfo.objects.first()
        profile_data = \
        {
            "profile_0":
            {
                "enabled": video_info.enabled_main,
                "encode":
                    {
                        "resolution":
                            {
                                "height": video_info.resolution_height_main,
                                "width": video_info.resolution_width_main
                            }
                    },
                "encode_profile": 1,
                "encode_type": video_info.encode_type_main,
                "framerate": video_info.frame_rate_main,
                "gop": video_info.gop_main,
                "jpeg_quality": video_info.jpeg_quality_main,
                "name": video_info.url_main,
                "quality":
                    {
                        "max": DeviceVideoInfo._meta.get_field('quality_main').validators[1].limit_value,
                        "min": DeviceVideoInfo._meta.get_field('quality_main').validators[0].limit_value,
                        "value": video_info.quality_main
                    },
                "ratecontrol": 
                    {
                        "bitrate": video_info.bit_rate_main,
                        "bitratemax": DeviceVideoInfo._meta.get_field('bit_rate_main').validators[1].limit_value,
                        "bitratemin": DeviceVideoInfo._meta.get_field('bit_rate_main').validators[0].limit_value,
                        "mode": video_info.video_encoding_main
                    },
                "resolution":
                    {
                        "height": video_info.resolution_height_main,
                        "width": video_info.resolution_width_main
                    }
            },
            "profile_1":
            {
                "enabled": video_info.enabled_sub,
                "encode":
                    {
                        "resolution":
                            {
                                "height": video_info.resolution_height_sub,
                                "width": video_info.resolution_width_sub
                            }
                    },
                "encode_profile": 1,
                "encode_type": video_info.encode_type_sub,
                "framerate": video_info.frame_rate_sub,
                "gop": video_info.gop_sub,
                "jpeg_quality": video_info.jpeg_quality_sub,
                "name": video_info.url_sub,
                "quality":
                    {
                        "max": DeviceVideoInfo._meta.get_field('quality_sub').validators[1].limit_value,
                        "min": DeviceVideoInfo._meta.get_field('quality_sub').validators[0].limit_value,
                        "value": video_info.quality_sub
                    },
                "ratecontrol": 
                    {
                        "bitrate": video_info.bit_rate_sub,
                        "bitratemax": DeviceVideoInfo._meta.get_field('bit_rate_sub').validators[1].limit_value,
                        "bitratemin": DeviceVideoInfo._meta.get_field('bit_rate_sub').validators[0].limit_value,
                        "mode": video_info.video_encoding_sub
                    },
                "resolution":
                    {
                        "height": video_info.resolution_height_sub,
                        "width": video_info.resolution_width_sub
                    }
            },
            "profile_2":
            {
                "enabled": video_info.enabled_third,
                "encode":
                    {
                        "resolution":
                            {
                                "height": video_info.resolution_height_third,
                                "width": video_info.resolution_width_third
                            }
                    },
                "encode_profile": 1,
                "encode_type": video_info.encode_type_third,
                "framerate": video_info.frame_rate_third,
                "gop": video_info.gop_third,
                "jpeg_quality": video_info.jpeg_quality_third,
                "name": video_info.url_third,
                "quality":
                    {
                        "max": DeviceVideoInfo._meta.get_field('quality_third').validators[1].limit_value,
                        "min": DeviceVideoInfo._meta.get_field('quality_third').validators[0].limit_value,
                        "value": video_info.quality_third
                    },
                "ratecontrol": 
                    {
                        "bitrate": video_info.bit_rate_third,
                        "bitratemax": DeviceVideoInfo._meta.get_field('bit_rate_third').validators[1].limit_value,
                        "bitratemin": DeviceVideoInfo._meta.get_field('bit_rate_third').validators[0].limit_value,
                        "mode": video_info.video_encoding_third
                    },
                "resolution":
                    {
                        "height": video_info.resolution_height_third,
                        "width": video_info.resolution_width_third
                    }
            }
        }

        return Response(profile_data)


class GetMultimediaValueImageView(APIView):
    def get(self, request):
        image_info = DeviceImageInfo.objects.first()
        imaging_data = \
        {
            "imaging_0":
                {
                    "brightness": image_info.brightness,
                    "brightness_in": DeviceImageInfo._meta.get_field('brightness').default,
                    "brightness_night": image_info.brightness_night,
                    "brightness_night_in": DeviceImageInfo._meta.get_field('brightness_night').default,
                    "bwmode": image_info.bw_mode,
                    "contrast": image_info.contrast,
                    "contrast_in": DeviceImageInfo._meta.get_field('contrast').default,
                    "contrast_night": image_info.contrast_night,
                    "contrast_night_in": DeviceImageInfo._meta.get_field('contrast_night').default,
                    "exposure":
                        {
                            "enabled": image_info.exposure_enabled,
                            "exp0": DeviceImageInfo._meta.get_field('day_exposure_gain').validators[0].limit_value,
                            "exp1": DeviceImageInfo._meta.get_field('day_exposure_gain').validators[1].limit_value,
                            "exposuretime": 
                                {
                                    "max": DeviceImageInfo._meta.get_field('day_exposure_time').validators[1].limit_value,
                                    "min": DeviceImageInfo._meta.get_field('day_exposure_time').validators[0].limit_value,
                                    "value": image_info.day_exposure_time
                                },
                            "gain":
                                {
                                    "max": DeviceImageInfo._meta.get_field('day_exposure_gain').validators[1].limit_value,
                                    "min": DeviceImageInfo._meta.get_field('day_exposure_gain').validators[0].limit_value,
                                },
                            "mode": image_info.day_mode_exposure,
                            "nightmode":
                                {
                                    "enabled": image_info.night_mode_exposure_enabled,
                                    "exp0": DeviceImageInfo._meta.get_field('night_exposure_gain').validators[0].limit_value,
                                    "exp1": DeviceImageInfo._meta.get_field('night_exposure_gain').validators[1].limit_value,
                                    "gain": image_info.night_exposure_gain,
                                    "gainmax": DeviceImageInfo._meta.get_field('night_exposure_gain').validators[1].limit_value,
                                }
                        },
                    "saturation": image_info.saturation,
                    "saturation_in": DeviceImageInfo._meta.get_field('saturation').default,
                    "saturation_night": image_info.saturation_night,
                    "saturation_night_in": DeviceImageInfo._meta.get_field('saturation_night').default,
                    "sharpness": image_info.sharpness,
                    "sharpness_in": DeviceImageInfo._meta.get_field('sharpness').default,
                    "sharpness_night": image_info.sharpness_night,
                    "sharpness_night_in": DeviceImageInfo._meta.get_field('sharpness_night').default,
                    "sensor":
                        {
                            "flip": image_info.flip,
                            "mirror": image_info.mirror
                        },
                    "wb":
                        {
                            "enable": image_info.wb_enabled,
                            "scenemode": image_info.wb_scene_mode,
                            "scenevalue": image_info.wb_scene_value
                        },
                    "wdr":
                        {
                            "enabled": image_info.wdr_enabled,
                            "value": image_info.wdr
                        },
                    "wdr_in":
                        {
                            "enabled": DeviceImageInfo._meta.get_field('wdr_enabled').default,
                            "value": DeviceImageInfo._meta.get_field('wdr').default
                        },
                    "wdr_night":
                        {
                            "enabled": image_info.wdr_night_enabled,
                            "value": image_info.wdr_night
                        },
                    "wdr_night_in":
                        {
                            "enabled": DeviceImageInfo._meta.get_field('wdr_night_enabled').default,
                            "value": DeviceImageInfo._meta.get_field('wdr_night').default
                        }
                }
        }
        
        return Response(imaging_data)
    
    
class SetMultimediaValueVideoView(APIView):
    def post(self, request):
        json_data = json.loads(request.body)
        print(json_data)
        
        return Response({})