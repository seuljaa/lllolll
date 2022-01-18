from django.urls import path
from . import views

app_name = "photo"

urlpatterns = [
    path('photo_list/', views.photo_list, name='photo_list'),
    path('photo_post/', views.photo_post, name='photo_post'),
]