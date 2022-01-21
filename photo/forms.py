from django import forms
from .models import Photo_post

from django_summernote.widgets import SummernoteWidget



class Photo_PostForm(forms.ModelForm):
    class Meta:
        model = Photo_post
        fields = ['content']

        labels = {
            'content': '내용'
        }