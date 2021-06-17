import os

# Core
ALLOWED_FILE_EXTENSIONS = ('.txt',)
SPLIT_TEXT_BY = os.getenv('SPLIT_TEXT_BY', ' ')

# Tests
FILENAME_FOR_TESTS = 'some_file' + ALLOWED_FILE_EXTENSIONS[0]
