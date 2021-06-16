from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileSerializer


class UploadFileView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            instance = file_serializer.save()
            words_occurrences = instance.get_words_occurrences()
            instance.delete()
            return Response(
                words_occurrences, status=status.HTTP_201_CREATED
            )
        return Response(
            file_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
