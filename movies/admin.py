from django.contrib import admin
from .models import Category, Movie, Recommendation, Review, History, FavoriteList, WatchLaterList

# Register your models here.

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Recommendation)
admin.site.register(Review)
admin.site.register(History)
admin.site.register(FavoriteList)
admin.site.register(WatchLaterList)
