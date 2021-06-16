import os

from django.conf import settings
from django.test import TestCase

from ..constants import FILENAME_FOR_TESTS
from ..factories import FileFactory


class FileModelTests(TestCase):
    def test_str(self):
        some_file = FileFactory()
        self.assertEqual(str(some_file), FILENAME_FOR_TESTS)

    def tearDown(self):
        os.remove(settings.MEDIA_ROOT / FILENAME_FOR_TESTS)
