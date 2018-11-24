from django import forms
from .models import Language, Module
from django_summernote.widgets import SummernoteWidget


class NewLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        widgets = {
            'description': SummernoteWidget(),
        }
        fields = (
            'title',
            'image',
            'description',
        )


class NewModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        widgets = {
            'description': SummernoteWidget(),
            'content': SummernoteWidget(),
        }
        fields = (
            'title',
            'language',
            'description',
            'price',
            'content',
            'release_date',
        )
