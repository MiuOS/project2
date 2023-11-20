from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    new_movies_notification = models.BooleanField(default=True)
    pass

