from rest_framework import serializers

from .models import *

class StorageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageInfo
        fields = '__all__'