from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login as auth_login, login
from django.contrib import messages
from django.contrib import admin

# Create your views here.
from .models import User


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save(commit=False)
            signed_user.is_active = False
            signed_user.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 신청이 완료되었습니다.")
            # signed_user.send_welcome_email()  # FIXME: Celery로 처리하는 것을 추천.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form} )

