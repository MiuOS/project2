from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

class EditProfileForm(forms.ModelForm):
    new_movies_notification = forms.BooleanField(required=False)
    new_movies_notification.label = "Powiadomienia o nowych filmach"

    card_number = forms.CharField(required=False)
    card_number.label = "Numer karty"

    card_expiration = forms.CharField(required=False)
    card_expiration.label = "Data ważności"

    card_cvv = forms.CharField(required=False)
    card_cvv.label = "CVV"

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'new_movies_notification', 'card_number', 'card_expiration', 'card_cvv')

class LoginForm(AuthenticationForm):
    pass