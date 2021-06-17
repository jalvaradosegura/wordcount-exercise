from ..factories import FileFactory
from ..models import File
from .utils import BaseForTests


class FileFactoryTests(BaseForTests):
    def test_create_an_instance(self):
        self.some_file = FileFactory()
        self.assertEqual(File.objects.count(), 1)
