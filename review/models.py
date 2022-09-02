from django.db import models


class recomendationOptions(models.TextChoices):
    must_watch = "Must Watch"
    should_watch = "Should Watch"
    avoid_watch = "Avoid Watch"
    DEFAULT = "No Opinion"

class Movie(models.Model):
    spoilers = models.BooleanField(null=True, blank=True)
    stars = models.IntegerField()
    review = models.TextField()
    recomendation = models.CharField(max_length=50, choices=recomendationOptions.choices, default=recomendationOptions.DEFAULT)
    movie_id = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )
    critic_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
