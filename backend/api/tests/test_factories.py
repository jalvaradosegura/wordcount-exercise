from .utils import BaseForTests
from ..factories import FileFactory
from ..models import File


class FileFactoryTests(BaseForTests):
    def test_create_an_instance(self):
        self.some_file = FileFactory()
        self.assertEqual(File.objects.count(), 1)
