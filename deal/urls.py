from django.urls import path
from . import views

app_name = 'deal'

urlpatterns = [
    path('list/', views.deal_list, name='deal_list')
]