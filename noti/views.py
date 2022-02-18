from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment
from .models import Noti, Noti_item
from photo.models import Photo_post
from deal.models import DealItems
from job.models import Post_job


# Create your views here.


def noti_reply():
    noti = Noti.objects.all()
    return noti

def noti_list(request):
    noti_list = Noti.objects.filter(to_user_id=request.user.id)
    return render(request, 'noti/noti_list.html', {'noti_list':noti_list})