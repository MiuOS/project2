from django.core.management.base import BaseCommand
from django.utils import timezone

from payments.models import Subscription, create_payment

class Command(BaseCommand):
    help = 'Description of your command'

    def handle(self, *args, **kwargs):
        subscriptions = Subscription.objects.filter(next_payment__lt=timezone.now(), status='active')

        for subscription in subscriptions:
            create_payment(subscription)
            print(f"Subscription done: {subscription}")