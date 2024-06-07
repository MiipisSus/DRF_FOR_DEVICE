from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from api.permissions import *

class GetStorageInfoView(APIView):
    permission_classes = [IsViewer]
    
    def get(self, request):
        storage_info = StorageInfo.objects.first()
        serializer = StorageInfoSerializer(storage_info)
        
        return Response(serializer.data)


class SetStorageInfoView(APIView):
    permission_classes = [IsEditor]
    
    def post(self, request):
        storage_info = StorageInfo.objects.first()
        serializer = StorageInfoSerializer(storage_info, request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)