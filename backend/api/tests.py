from django.urls import resolve, reverse
from django.test import TestCase

from .views import UploadFileView


class UploadFileViewTests(TestCase):
    def test_uses_the_correct_view(self):
        response = resolve(reverse('upload_file'))
        self.assertEqual(
            response.func.__name__, UploadFileView.as_view().__name__
        )
