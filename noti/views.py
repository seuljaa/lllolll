from django.shortcuts import render
from django.http import HttpResponse
from comment.models import Comment

# Create your views here.


def noti_reply(request, object_id):
    id = Comment.objects.last().id
    return HttpResponse(id)