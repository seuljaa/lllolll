from django.urls import path
from . import views

app_name = 'deal'

urlpatterns = [
    path('deal_list/', views.deal_list, name='deal_list'),
    path('post_Armor/', views.post_Armor, name='post_Armor'),
    path('deal_list/', views.deal_list, name='deal_list'),
    path('deal_list_gita/', views.deal_list_gita, name='deal_list_gita'),
    path('deal_detail/<int:deal_id>/', views.deal_detail, name='deal_detail'),
]
