from django import forms
from django.forms import TextInput
from django.forms import Select

from .models import Post_job

from django_summernote.widgets import SummernoteWidget



class PostForm(forms.ModelForm):
    class Meta:
        model = Post_job
        CHOICES = (
            ('1', '구인'),
            ('0', '구직'),
        )
        fields = ['content', 'subject', 'kind']
        widgets = {
            'content' : SummernoteWidget(),
            'subject' : TextInput(attrs={
                'class' : "gSearch t-w-[80%]",
                'placeholder' : "제목을 입력해주세요.",
                'onfocus' : "this.placeholder=''",
                'onblur' : "this.placeholder='제목을 입력해주세요.'",
                'id' : "subject",
                'name' : "subject"}),
            'kind' : Select(choices=CHOICES)
        }
        labels = {
            'content': '내용'
        }