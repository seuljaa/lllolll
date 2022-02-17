from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment
from .models import Noti, Noti_item


# Create your views here.


def noti_reply():
    noti = Noti.objects.all()
    return noti
