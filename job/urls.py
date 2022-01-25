from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('list/', views.job_list, name='job_list'),
    path('post_job/', views.post_job, name='post_job'),
    path('job_detail/<int:post_id>/', views.job_detail, name='job_detail'),
]
