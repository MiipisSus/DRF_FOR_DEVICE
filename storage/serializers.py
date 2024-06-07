from rest_framework import serializers

from .models import *


class StorageInfoSerializer(serializers.ModelSerializer):
    total_size = serializers.IntegerField(read_only=True)
    used_size = serializers.IntegerField(read_only=True)
    disk_status = serializers.BooleanField(read_only=True)
    record_file_type = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = StorageInfo
        fields = '__all__'
        
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if value is not None:
                setattr(instance, field, value)
                
        instance.save()
        
        return instance