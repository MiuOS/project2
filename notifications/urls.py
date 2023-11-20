from .views import get_notifications
from django.urls import path

urlpatterns = [
    path('', get_notifications, name='get_notifications'),
]
