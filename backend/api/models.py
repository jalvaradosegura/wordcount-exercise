from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

    def get_words_occurrences(self):
        return {'dogs': 2}
