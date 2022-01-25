from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms

from accounts.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = True
        self.fields['server'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'server']
        labels = {
            'username' : '메이플 닉네임(본캐)',
            'server' : '서버',
            'email':'이메일(비밀번호 찾을때 사용)',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            qs = User.objects.filter(username=username)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 닉네임 입니다.")
        return username