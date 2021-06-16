import os

from django.conf import settings
from django.test import TestCase

from ..constants import FILENAME_FOR_TESTS
from ..factories import FileFactory
from ..models import File


class FileFactoryTests(TestCase):
    def test_create_an_instance(self):
        self.some_file = FileFactory()
        self.assertEqual(File.objects.count(), 1)

    def tearDown(self):
        os.remove(settings.MEDIA_ROOT / FILENAME_FOR_TESTS)
