from django import forms
from .models import DealItems

from django_summernote.widgets import SummernoteWidget



class PostForm(forms.ModelForm):
    class Meta:
        model = DealItems
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'content': '내용'
        }