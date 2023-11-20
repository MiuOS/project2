from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from notifications.models import Notification


# Create your views here.

@login_required(login_url='login')
def get_notifications(request):
    notiffications = Notification.objects.filter(user=request.user, is_read=False, date__lte=timezone.now()).order_by('-date')

    # Convert the notifications into a format that can be serialized
    notifications_data = []

    for notification in notiffications:
        notifications_data.append({
            'id': notification.id,
            'title': notification.template.title,
            'content': notification.template.content,
            'color': notification.get_color()
        })
        notification.is_read = True
        notification.save()

    return JsonResponse({'notifications': notifications_data})