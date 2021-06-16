import os

from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)

    def validate_file(self, value):
        file_name = str(value)
        ext = os.path.splitext(file_name)[1]
        if not ext.lower() in ['.txt']:
            raise serializers.ValidationError('Not a valid file extension')
        return value
