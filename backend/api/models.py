from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

    def get_words_occurrences(self):
        file_content = str(self.file.read(), 'utf-8')
        chars_to_replace = '?¿()[]{}><!$.,\'\"\n\t'
        for c in chars_to_replace:
            file_content = file_content.replace(c, '')
        words = file_content.split(' ')
        return {word: words.count(word) for word in words}
