from django.urls import path
from . import views

app_name = "noti"

urlpatterns = [
    path('reply/<int:object_id>/', views.noti_reply, name='noti_reply'),
    path('noti_list/', views.noti_list, name='noti_list'),
]
