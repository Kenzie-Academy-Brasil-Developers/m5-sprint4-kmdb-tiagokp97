
from django.contrib.auth.models import AbstractUser
from django.db import models


class criticOptions(models.TextChoices):
    CRITIC = True
    DEFAULT = False


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField()
    is_critic = models.CharField(max_length=5, choices=criticOptions.choices, default=criticOptions.DEFAULT)


    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "birthdate", ]

