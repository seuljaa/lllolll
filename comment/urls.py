from django.urls import path
from . import views

app_name='comment'

urlpatterns = [
    path('photo/<int:photo_id>/', views.comment_photo, name='comment_photo'),
]