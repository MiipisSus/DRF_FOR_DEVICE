from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class GetStorageInfoView(APIView):
    def get(self, request):
        storage_info = StorageInfo.objects.first()
        serializer = StorageInfoSerializer(storage_info)
        
        return Response(serializer.data)