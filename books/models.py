from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title