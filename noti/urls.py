from django.urls import path
from . import views

app_name = "noti"

urlpatterns = [
    path('reply/<int:object_id>/', views.noti_reply, name='noti_reply'),
    path('noti_list/', views.noti_list, name='noti_list'),
    path('noti_check/<int:article_ct_id>/<int:article_id>/<int:noti_id>/', views.noti_check, name='noti_check'),
    path('all_check/', views.all_check, name='all_check'),
]
