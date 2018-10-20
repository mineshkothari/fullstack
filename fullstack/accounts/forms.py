from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(attrs={'placeholder': 'email address'})
    )

    password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )

    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'password confirmation'})
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(attrs={'placeholder': 'email address'})
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'password'})
    )


class UserAccountForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2040)]

    email = forms.EmailField(widget=forms.EmailInput)
    display_name = forms.CharField(label='Display Name')
    card_number = forms.CharField(label='Card Number')
    cvv = forms.CharField(label='CVV')
    expiry_month = forms.ChoiceField(label="Expiry Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Expiry Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ['email',  'stripe_id']
        # exclude = ['username']
