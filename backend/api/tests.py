import os

from django.conf import settings
from django.test import TestCase
from django.urls import resolve, reverse

from .constants import FILENAME_FOR_TESTS
from .factories import FileFactory
from .models import File
from .views import UploadFileView


class UploadFileViewTests(TestCase):
    def test_uses_the_correct_view(self):
        response = resolve(reverse('upload_file'))
        self.assertEqual(
            response.func.__name__, UploadFileView.as_view().__name__
        )


class FileModelTests(TestCase):
    def test_str(self):
        some_file = FileFactory()
        self.assertEqual(str(some_file), FILENAME_FOR_TESTS)

    def tearDown(self):
        os.remove(settings.MEDIA_ROOT / FILENAME_FOR_TESTS)


class FileFactoryTests(TestCase):
    def test_create_an_instance(self):
        self.some_file = FileFactory()
        self.assertEqual(File.objects.count(), 1)

    def tearDown(self):
        os.remove(settings.MEDIA_ROOT / FILENAME_FOR_TESTS)
