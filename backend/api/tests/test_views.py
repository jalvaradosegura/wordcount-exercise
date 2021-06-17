from http import HTTPStatus

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import resolve, reverse

from ..constants import FILENAME_FOR_TESTS
from ..views import UploadFileView
from .utils import BaseForTests


class UploadFileViewTests(BaseForTests):
    def test_uses_the_correct_view(self):
        response = resolve(reverse('upload_file'))
        self.assertEqual(
            response.func.__name__, UploadFileView.as_view().__name__
        )

    def test_post_request_success(self):
        some_file = SimpleUploadedFile(
            FILENAME_FOR_TESTS, b'This is some awesome content'
        )

        response = self.client.post(
            reverse('upload_file'), data={'file': some_file}
        )

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response.json()['awesome'], 1)

    def test_post_request_fail_due_bad_file_extension(self):
        some_file = SimpleUploadedFile(
            'this_file_has_an_invalid_extension.pdf',
            b'This is some awesome content',
        )

        response = self.client.post(
            reverse('upload_file'), data={'file': some_file}
        )

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(
            response.json()['file'], ['Not a valid file extension']
        )
