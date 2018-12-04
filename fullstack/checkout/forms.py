from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2040)]

    # USE 'required=False' TO PREVENT PLAIN TEXT BEING TRANSMITTED THROUGH BROWSER
    card_number = forms.CharField(label='Card Number', required=False)
    cvv = forms.CharField(label='CVV', required=False)
    expiry_month = forms.ChoiceField(label="Expiry Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Expiry Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'user',
            'is_ordered',
            'date_ordered'
        )
