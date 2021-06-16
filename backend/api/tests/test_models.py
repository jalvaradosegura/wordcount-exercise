import os

from django.conf import settings
from django.test import TestCase

from ..constants import FILENAME_FOR_TESTS
from ..factories import FileFactory


class FileModelTests(TestCase):
    def test_str(self):
        some_file = FileFactory()
        self.assertEqual(str(some_file), FILENAME_FOR_TESTS)

    def test_get_words_occurrences(self):
        some_file = FileFactory(file__data='dogs are cool, dogs are great')
        self.assertEqual(some_file.get_words_occurrences()['dogs'], 2)

    def tearDown(self):
        os.remove(settings.MEDIA_ROOT / FILENAME_FOR_TESTS)
