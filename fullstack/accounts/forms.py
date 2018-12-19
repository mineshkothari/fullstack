from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class UserAccountForm(forms.ModelForm):

    display_name = forms.CharField(label='Display Name')

    class Meta:
        model = User
        # User Editable Fields
        fields = [
            'first_name',
            'last_name',
            'display_name',
            'email',
        ]
        # Excluded Fields
        exclude = ['username']
