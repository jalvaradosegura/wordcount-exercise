import numpy as np
from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

    def get_words_occurrences(self):
        file_content = str(self.file.read(), 'utf-8')
        file_content = file_content.replace('\n', ' ').replace('\t', ' ')

        chars_to_replace = '`´:º#?¿()[]{}><!$.,@&\'\"\\'
        for c in chars_to_replace:
            file_content = file_content.replace(c, '')

        words = list(filter(None, file_content.split(' ')))

        # Note: version using standard Python
        # return {word: words.count(word) for word in words}

        x = np.array(words)
        unique, counts = np.unique(x, return_counts=True)

        return {unique[i]: count for i, count in enumerate(counts)}
