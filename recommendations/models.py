from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    poster_url = models.URLField()
    release_date = models.DateField()
