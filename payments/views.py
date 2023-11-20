from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from payments.forms import SubscriptionForm
from payments.models import Subscription


# Create your views here.

@login_required
def change_subscription(request):
    # Retrieve the existing subscription for the user
    subscription = Subscription.objects.filter(user=request.user).first()

    if request.method == 'POST':
        # Initialize the form with POST data and bind it to the existing instance
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            # The form will now update the existing subscription instance
            updated_subscription = form.save(commit=False)
            updated_subscription.next_payment = updated_subscription.get_next_payment()
            updated_subscription.user = request.user
            updated_subscription.save()
            return redirect('profile', username=request.user.username)
        else:
            # If the form is not valid, render the form with errors
            return render(request, 'payments/change_subscription.html', {'form': form})
    else:
        # If it's a GET request, initialize the form with the existing instance
        form = SubscriptionForm(instance=subscription)
        return render(request, 'payments/change_subscription.html', {'form': form})