from django import forms

from .models import Payment, Subscription, SubscriptionType


class SubscriptionForm(forms.ModelForm):
    subscription = forms.ModelChoiceField(
        queryset=SubscriptionType.objects.all(),
        widget=forms.Select(attrs={'class': 'select'})  # Add Bulma 'select' class
    )

    subscription.label = 'Typ subskrypcji'

    class Meta:
        model = Subscription
        fields = ('subscription',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        # Apply Bulma classes to each form field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'  # Bulma 'input' class for all fields