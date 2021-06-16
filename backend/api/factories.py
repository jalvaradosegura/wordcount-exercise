import factory

from .constants import FILENAME_FOR_TESTS


class FileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.File'

    file = factory.django.FileField(filename=FILENAME_FOR_TESTS)
