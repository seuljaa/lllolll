from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('list/', views.job_list, name='job_list'),
    path('post_job/', views.post_job, name='post_job'),
    path('job_detail/<int:post_id>/', views.job_detail, name='job_detail'),
    path('job_complete/<int:post_id>/', views.job_complete, name='job_complete'),
    path('job_delete/<int:post_id>/', views.job_delete, name='job_delete'),
    path('job_modify/<int:post_id>/', views.job_modify, name='job_modify'),
]
