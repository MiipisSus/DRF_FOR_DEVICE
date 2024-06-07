from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from api.permissions import *


class GetBasicDeviceInfo(APIView):
    permission_classes = [IsViewer]
    
    def get(self, request):
        basic_device_info = DeviceBasicInfo.objects.first()
        serializer = DeviceBasicInfoSerializer(basic_device_info)
        return Response(serializer.data)


class SetBasicDeviceInfo(APIView):
    permission_classes = [IsEditor]
    
    def post(self, request):
        basic_device_info = DeviceBasicInfo.objects.first()
        serializer = DeviceBasicInfoSerializer(basic_device_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        

class GetNetworkInfo(APIView):
    permission_classes = [IsViewer]
    
    def get(self, request):
        network_info = DeviceNetworkInfo.objects.all()
        serializer = DeviceNetworkInfoSerializer(network_info)
        return Response(serializer.data)


class SetNetworkInfo(APIView):
    permission_classes = [IsEditor]
    
    def post(self, request):
        network_info = DeviceNetworkInfo.objects.first()
        serializer = DeviceNetworkInfoSerializer(network_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
    

class GetOSDInfo(APIView):
    permission_classes = [IsViewer]
    
    def get(self, request):
        osd_info = DeviceOSDInfo.objects.first()
        serializer = DeviceOSDInfoSerializer(osd_info)
        return Response(serializer.data)


class SetOSDInfo(APIView):
    permission_classes = [IsEditor]
    
    def post(self, request):
        osd_info = DeviceOSDInfo.objects.first()
        serializer = DeviceOSDInfoSerializer(osd_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)


class GetMultimediaValueVideoView(APIView):
    permission_classes = [IsViewer]
    
    def get(self, request):
        video_info = DeviceVideoInfo.objects.first()
        serializer = DeviceVideoInfoSerializer(video_info)

        return Response(serializer.data)


class GetMultimediaValueImageView(APIView):
    permission_classes = [IsViewer]
    
    def get(self, request):
        image_info = DeviceImageInfo.objects.first()
        serializer = DeviceImageInfoSerializer(image_info)
        
        return Response(serializer.data)
    
    
class SetMultimediaValueVideoView(APIView):
    permission_classes = [IsEditor]
    
    def post(self, request):
        video_info = DeviceVideoInfo.objects.first()
        serializer = DeviceVideoInfoSerializer(video_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        
        
class SetMultimediaValueImageView(APIView):
    permission_classes = [IsEditor]
    
    def post(self, request):
        image_info = DeviceImageInfo.objects.first()
        serializer = DeviceImageInfoSerializer(image_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        
        
