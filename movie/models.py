from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=127, unique=True)
    duration = models.EmailField(max_length=10, unique=True)
    premiere = models.DateField(null=True, blank=True)
    classification = models.IntegerField()
    synopsis = models.TextField()
    genres = models.ManyToManyField("genres.Genre", related_name="movies")


