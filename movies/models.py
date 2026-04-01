from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    duration = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.title
