from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('photo/<int:photo_id>/', views.comment_photo, name='comment_photo'),
    path('deal/<int:deal_id>/', views.comment_deal, name='comment_deal'),
    path('job/<int:job_id>/', views.comment_job, name='comment_job'),
]
