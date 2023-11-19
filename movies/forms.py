from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):
    RATING_CHOICES = [(str(i), str(i)) for i in range(0, 11)]

    text = forms.CharField(widget=forms.Textarea, label='Recenzja')
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        label='Ocena'
    )

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # Add Bulma classes to the textarea
        self.fields['text'].widget.attrs.update({'class': 'textarea'})

        # Add custom class for inline display to the radio buttons
        self.fields['rating'].widget.attrs.update({'class': 'inline-radio'})

    class Meta:
        model = Review
        fields = ['rating', 'text']