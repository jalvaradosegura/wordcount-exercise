from ..constants import FILENAME_FOR_TESTS
from ..factories import FileFactory
from .utils import BaseForTests


class FileModelTests(BaseForTests):
    def test_str(self):
        some_file = FileFactory()
        self.assertEqual(str(some_file), FILENAME_FOR_TESTS)

    def test_get_words_occurrences_simple_text(self):
        some_file = FileFactory(file__data='dogs are cool?, dogs are great!')
        self.assertEqual(
            some_file.get_words_occurrences(),
            {'dogs': 2, 'are': 2, 'cool': 1, 'great': 1},
        )

    def test_get_words_occurrences_text_has_new_lines_and_tabs(self):
        some_file = FileFactory(
            file__data='dogs are cool?,\n dogs are \ngreat\t!'
        )
        self.assertEqual(
            some_file.get_words_occurrences(),
            {'dogs': 2, 'are': 2, 'cool': 1, 'great': 1},
        )

    def test_get_words_occurrences_text_has_a_lot_of_symbols(self):
        some_file = FileFactory(
            file__data=(
                '#dogs are `cool?,\n dogs & cats are \ngreat\t! & @user @user'
            )
        )
        self.assertEqual(
            some_file.get_words_occurrences(),
            {'dogs': 2, 'are': 2, 'cool': 1, 'great': 1, 'cats': 1, 'user': 2},
        )
