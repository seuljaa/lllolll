from django import forms
from .models import Photo_post

from django_summernote.widgets import SummernoteWidget



class Photo_PostForm(forms.ModelForm):
    class Meta:
        model = Photo_post
        fields = ['content', 'imgfile']

        labels = {
            'content': '내용',
            'imgfile': '이미지업로드'
        }