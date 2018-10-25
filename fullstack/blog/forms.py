from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'content': SummernoteWidget(),
        }
        fields = ('title', 'content', 'tag', 'image')
