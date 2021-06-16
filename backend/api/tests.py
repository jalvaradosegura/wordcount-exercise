import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import resolve, reverse

from .models import File
from .views import UploadFileView


class UploadFileViewTests(TestCase):
    def test_uses_the_correct_view(self):
        response = resolve(reverse('upload_file'))
        self.assertEqual(
            response.func.__name__, UploadFileView.as_view().__name__
        )


class FileModelTests(TestCase):
    filename = 'some_file.txt'

    def test_str(self):
        some_file = File.objects.create(
            file=SimpleUploadedFile(self.filename, b'hello world')
        )
        self.assertEqual(str(some_file), 'some_file.txt')

    def tearDown(self):
        os.remove(self.filename)
