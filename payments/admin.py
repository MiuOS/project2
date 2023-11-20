from django.contrib import admin
from .models import Payment, Subscription, SubscriptionType

# Register your models here.

admin.site.register(Payment)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)