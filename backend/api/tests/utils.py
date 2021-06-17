import os

from django.conf import settings
from django.test import TestCase

from ..constants import FILENAME_FOR_TESTS


class BaseForTests(TestCase):
    def tearDown(self):
        try:
            os.remove(settings.MEDIA_ROOT / FILENAME_FOR_TESTS)
        except FileNotFoundError:
            pass
