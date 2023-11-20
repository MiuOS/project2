from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.dispatch import receiver

from notifications.models import NotificationTemplate, Notification, create_notification
from users.models import CustomUser
from django.db.models.signals import pre_delete, post_save

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class History(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="history")
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="history")
#
    def __str__(self):
        return f"{self.user} - {self.movie}"

class FavoriteList(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="favorite_list")
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="favorite_list")

    def __str__(self):
        return f"{self.user} - {self.movie}"

class WatchLaterList(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="watch_later_list")
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="watch_later_list")
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.movie}"

class Recommendation(models.Model):
    movie = models.OneToOneField("Movie", on_delete=models.CASCADE, related_name="recommendations")

    def __str__(self):
        return f"{self.movie}"

class Review(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.movie} - {self.user}"

class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    year = models.IntegerField()
    category = models.ManyToManyField(Category, blank=True, related_name="movies")
    file = models.FileField(upload_to="movies/", blank=True, null=True)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    large_cover = models.ImageField(upload_to="large_covers/", blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

    def send_notification_before_deleted(self):
        # Fetch users who have this movie in their watch later list
        users_watch_later = CustomUser.objects.filter(watch_later_list__movie=self)
        # Fetch users who have this movie in their favorite list
        users_favorite = CustomUser.objects.filter(favorite_list__movie=self)

        # Then, send notifications
        if users_watch_later:
            create_notification(
                users_watch_later,
                f"Usunięto interesującą Cię pozycję.",
                f"Film o tytule \"{self.title}\" został usunięty.",
                "is-info"
            )

        if users_favorite:
            create_notification(
                users_favorite,
                f"Usunięto jedną z Twoich ulubionych pozycji.",
                f"Film o tytule \"{self.title}\" został usunięty.",
                "is-info"
            )

    def send_notification_after_added(self):
        users = CustomUser.objects.filter(new_movies_notification=True)

        self._create_notification(
            users,
            f"Dodano nową pozycję!",
            f"Właśnie dodano nowy film o tytule \"{self.title}\"",
            "is-info"
        )

@receiver(pre_delete, sender=Movie)
def movie_pre_delete(sender, instance, **kwargs):
    instance.send_notification_before_deleted()

@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, **kwargs):
    instance.send_notification_after_added()
