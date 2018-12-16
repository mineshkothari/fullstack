from django import forms
from django.utils import timezone
from .models import Language, Module


class NewLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = (
            'title',
            'image',
            'description',
        )


class NewModuleForm(forms.ModelForm):

    release_date = forms.DateTimeField(initial=timezone.now(),
                                       widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M'))

    class Meta:
        model = Module
        fields = (
            'title',
            'language',
            'description',
            'price',
            'content',
            'release_date',
        )
