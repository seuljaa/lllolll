from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='accounts/sign_in.html'), name='sign_in'),
    path('sign_out/', auth_views.LogoutView.as_view(), name='sign_out'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]