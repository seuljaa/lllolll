from django.urls import path
from . import views

app_name = 'deal'

urlpatterns = [
    path('deal_list/', views.deal_list, name='deal_list'),
    path('post_Armor/', views.post_Armor, name='post_Armor'),
    path('deal_detail/<int:deal_id>/', views.deal_detail, name='deal_detail'),
    path('deal_gita_list/', views.deal_gita_list, name='deal_gita_list'),
    path('post_gita/', views.post_gita, name='post_gita'),
    path('deal_complete/<int:deal_id>/', views.deal_complete, name='deal_complete'),
    path('deal_delete/<int:deal_id>/', views.deal_delete, name='deal_delete'),
]
