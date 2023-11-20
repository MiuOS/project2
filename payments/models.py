import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone

# Create your models here.

subscription_status_choices = [
    ('active', 'Aktywny'),
    ('expired', 'Wygasł'),
    ('canceled', 'Anulowany'),
]

class SubscriptionType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    subscription = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=subscription_status_choices, default='active')
    next_payment = models.DateTimeField()
    wallet = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} - {self.subscription}"

    def get_next_payment(self):
        return timezone.now() + timedelta(days=self.subscription.duration)

class Payment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.subscription} - {self.status}"


def create_payment(subscription):
    value_needed = subscription.subscription.price - subscription.wallet
    user = subscription.user

    if value_needed > 0:
        # Assuming is_card_valid is a method in the CustomUser model that checks if the card is valid
        if user.is_card_valid():
            # Simulate payment processing
            payment_successful = process_payment(user, value_needed)  # This should be implemented

            if payment_successful:
                # Create a new payment record
                Payment.objects.create(
                    subscription=subscription,
                    status='successful',
                    transaction_id=str(uuid.UUID),  # Generate or obtain this ID from your payment processor
                    value=value_needed
                )
                # Update subscription and wallet
                subscription.wallet = 0
                subscription.status = 'active'
                subscription.next_payment = subscription.get_next_payment()
            else:
                # Handle failed payment
                subscription.status = 'expired'
        else:
            # Handle invalid card
            subscription.status = 'expired'
    else:
        # If the wallet balance covers the subscription
        subscription.wallet = abs(value_needed)
        subscription.status = 'active'
        subscription.next_payment = subscription.get_next_payment()

    # Save the updated subscription
    subscription.save()


def process_payment(user, amount):
    # Implement payment processing logic here
    # For simulation purposes, let's assume all payments are successful
    return True
