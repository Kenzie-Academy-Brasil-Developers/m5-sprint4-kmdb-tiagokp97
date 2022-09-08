from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RecomendationChoices(models.TextChoices):
  MUST = 'Must Watch'
  SHOULD = 'Should Watch'
  AVOID = 'Avoid Watch'
  NO = 'No Opinion'

class Review(models.Model):
  stars = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  review = models.TextField()
  spoilers = models.BooleanField(default=False)
  recomendation= models.CharField(max_length=50, choices=RecomendationChoices.choices, default=RecomendationChoices.NO)

  movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='reviews')
  critic = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reviews')
