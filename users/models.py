import calendar
from datetime import datetime, timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    new_movies_notification = models.BooleanField(default=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_expiration = models.CharField(max_length=5, blank=True, null=True)
    card_cvv = models.CharField(max_length=3, blank=True, null=True)
    pass

    def is_card_valid(self):
        if self.card_number and self.card_expiration and self.card_cvv:
            return True
        else:
            return False

    def get_exp_date(self):
        if self.card_expiration:
            month, year = self.card_expiration.split('/')
            year = int('20' + year)
            month = int(month)
            last_day = calendar.monthrange(year, month)[1]
            naive_datetime = datetime.datetime(year, month, last_day, 23, 59, 59)
            return timezone.make_aware(naive_datetime, timezone.get_default_timezone())
        else:
            return None


