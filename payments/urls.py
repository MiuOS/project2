from django.urls import path
from .views import change_subscription

urlpatterns = [
    path('change_subscription/', change_subscription, name='change_subscription'),
]