from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class History(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE, related_name="history")
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="history")

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