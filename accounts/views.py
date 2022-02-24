from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignupForm
from django.contrib.auth import login as auth_login, login
from django.contrib import messages

# Create your views here.
from .models import User
from .forms import FindUser

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

def find_id(request):
    form = FindUser()
    return render(request, 'accounts/find_id.html', {'form':form})

def find_id_complete(request):
    result = []
    username = []
    if request.method == 'POST':
        form = FindUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            qs: QuerySet = User.objects.filter(email=email)

            if not qs.exists():
                result.append(0)
                return render(request, 'accounts/find_id_complete.html', {'result': result})

            else:
                user: User = qs.first()
                result.append(1)
                username.append(user)
                return render(request, 'accounts/find_id_complete.html', {'result': result, 'username': username} )