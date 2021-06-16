from django.urls import path

from .views import UploadFileView

urlpatterns = [
    path(
        route='upload_file/',
        view=UploadFileView.as_view(),
        name='upload_file',
    ),
]
