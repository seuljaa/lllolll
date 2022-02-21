from django.contrib.auth.decorators import login_required
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

@login_required(login_url='accounts:sign_in')
def noti_list(request):
    article_list = []
    photo_content = ContentType.objects.get_for_model(Photo_post)
    job_content = ContentType.objects.get_for_model(Post_job)
    deal_content = ContentType.objects.get_for_model(DealItems)

    photo_noti = Noti.objects.filter(content_type=photo_content, to_user_id=request.user.id, is_viewed=0)
    job_noti = Noti.objects.filter(content_type=job_content, to_user_id=request.user.id, is_viewed=0)
    deal_noti = Noti.objects.filter(content_type=deal_content, to_user_id=request.user.id, is_viewed=0)
    noti_list = Noti.objects.filter(to_user_id=request.user.id, is_viewed=0)

    photo_list = Photo_post.objects.filter(user_id=request.user.id)

    for photo in photo_noti:
        article_list.append(Photo_post.objects.get(pk=photo.object_id))

    for job in job_noti:
        article_list.append(Post_job.objects.get(pk=job.object_id))

    for deal in deal_noti:
        article_list.append(DealItems.objects.get(pk=deal.object_id))



    return render(request, 'noti/noti_list.html', {'noti_list':noti_list, 'photo_list':photo_list})