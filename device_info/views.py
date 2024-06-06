from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

import json

class GetBasicDeviceInfo(APIView):
    def get(self, request):
        basic_device_info = DeviceBasicInfo.objects.first()
        serializer = DeviceBasicInfoSerializer(basic_device_info)
        return Response(serializer.data)


class SetBasicDeviceInfo(APIView):
    def post(self, request):
        basic_device_info = DeviceBasicInfo.objects.first()
        serializer = DeviceBasicInfoSerializer(basic_device_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        

class GetNetworkInfo(APIView):
    def get(self, request):
        network_info = DeviceNetworkInfo.objects.all()
        serializer = DeviceNetworkInfoSerializer(network_info)
        return Response(serializer.data)


class SetNetworkInfo(APIView):
    def post(self, request):
        network_info = DeviceNetworkInfo.objects.first()
        serializer = DeviceNetworkInfoSerializer(network_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
    

class GetOSDInfo(APIView):
    def get(self, request):
        osd_info = DeviceOSDInfo.objects.first()
        serializer = DeviceOSDInfoSerializer(osd_info)
        return Response(serializer.data)


class SetOSDInfo(APIView):
    def post(self, request):
        osd_info = DeviceOSDInfo.objects.first()
        serializer = DeviceOSDInfoSerializer(osd_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)


class GetMultimediaValueVideoView(APIView):
    def get(self, request):
        video_info = DeviceVideoInfo.objects.first()
        serializer = DeviceVideoInfoSerializer(video_info)
        '''
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
        '''

        return Response(serializer.data)


class GetMultimediaValueImageView(APIView):
    def get(self, request):
        image_info = DeviceImageInfo.objects.first()
        serializer = DeviceImageInfoSerializer(image_info)
        
        return Response(serializer.data)
    
    
class SetMultimediaValueVideoView(APIView):
    def post(self, request):
        video_info = DeviceVideoInfo.objects.first()
        serializer = DeviceVideoInfoSerializer(video_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        
        
class SetMultimediaValueImageView(APIView):
    def post(self, request):
        image_info = DeviceImageInfo.objects.first()
        serializer = DeviceImageInfoSerializer(image_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        # try:
        #     data = request.data
        #     self.update_instance(data)
        #     response = Response({"message": "Update image info success."}, status=200)
        # except:
        #     response = Response({"message": "Update image info failed."}, status=400)

        # return response
    
    def update_instance(self, data):
        image_info = DeviceImageInfo.objects.first()
        
        def update_if_not_None(field, value):
            if value is not None:
                setattr(image_info, field, value)
                
        def update_imaging(imaging_data):
            update_if_not_None('brightness', imaging_data.get('brightness'))
            update_if_not_None('brightness_night', imaging_data.get('brightness_night'))
            update_if_not_None('bwmode', imaging_data.get('bw_mode'))
            update_if_not_None('contrast', imaging_data.get('contrast'))
            update_if_not_None('contrast_night', imaging_data.get('contrast_night'))
            
            exposure = imaging_data.get('exposure')
            if exposure:
                update_if_not_None('exposure_enabled', exposure.get('enabled'))
                
                exposure_time = exposure.get('exposuretime')
                if exposure_time:
                    update_if_not_None('day_exposure_time', exposure_time.get('value'))
                
                update_if_not_None('day_mode_exposure', exposure.get('mode'))
                
                gain = exposure.get('gain')
                if gain:
                    update_if_not_None('day_exposure_gain', gain.get('value'))
                
                nightmode = exposure.get('nightmode')
                if nightmode:
                    update_if_not_None('night_mode_exposure_enabled', nightmode.get('enabled'))
                    update_if_not_None('night_exposure_gain', nightmode.get('gain'))
            
            update_if_not_None('saturation', imaging_data.get('saturation'))
            update_if_not_None('saturation_night', imaging_data.get('saturation_night'))
            update_if_not_None('sharpness', imaging_data.get('sharpness'))
            update_if_not_None('sharpness_night', imaging_data.get('sharpness_night'))
            
            sensor = imaging_data.get('sensor')
            if sensor:
                update_if_not_None('flip', sensor.get('flip'))
                update_if_not_None('mirror', sensor.get('mirror'))
            
            wb = imaging_data.get('wb')
            if wb:
                update_if_not_None('wb_enabled', wb.get('enable'))
                update_if_not_None('wb_scene_mode', wb.get('scenemode'))
                update_if_not_None('wb_scene_value', wb.get('scenevalue'))
                
            wdr = imaging_data.get('wdr')
            if wdr:
                update_if_not_None('wdr_enabled', wdr.get('enable'))
                update_if_not_None('wdr', wdr.get('value'))
            
            wdr_night = imaging_data.get('wdr_night')
            if wdr:
                update_if_not_None('wdr_night_enabled', wdr_night.get('enable'))
                update_if_not_None('wdr_night', wdr_night.get('value'))
            
        
        update_imaging(data.get('imaging_0'))
        
        image_info.save()
        
        
