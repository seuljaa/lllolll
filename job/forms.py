from django import forms
from .models import Post_job

from django_summernote.widgets import SummernoteWidget



class PostForm(forms.ModelForm):
    class Meta:
        model = Post_job
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'content': '내용'
        }