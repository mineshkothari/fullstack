from django import forms
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
