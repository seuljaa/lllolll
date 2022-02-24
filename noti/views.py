from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
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

    noti_list = Noti.objects.filter(to_user_id=request.user.id, is_viewed=0).order_by('create_date')

    for noti in noti_list :
        if noti.content_type == photo_content:
            article = Photo_post.objects.get(pk=noti.object_id)
            if article not in article_list:
                article_list.append(Photo_post.objects.get(pk=noti.object_id))

        if noti.content_type == job_content:
            article = Post_job.objects.get(pk=noti.object_id)
            if article not in article_list:
                article_list.append(Post_job.objects.get(pk=noti.object_id))

        if noti.content_type == deal_content:
            article = DealItems.objects.get(pk=noti.object_id)
            if article not in article_list:
                article_list.append(DealItems.objects.get(pk=noti.object_id))

    return render(request, 'noti/noti_list.html', {'noti_list':noti_list, 'article_list':article_list})

def noti_check(request, article_ct_id, article_id, noti_id):
    noti = Noti.objects.get(pk=noti_id)
    noti.is_viewed = 1
    noti.save()
    if article_ct_id == 13 :
        return redirect('job:job_detail', article_id)
    if article_ct_id == 8 :
        article = DealItems.objects.get(pk=article_id)
        if article.category == 1 :
            return redirect('deal:deal_detail', article_id)
        else :
            return redirect('deal:deal_gita_detail', article_id)
    if article_ct_id == 10 :
        return redirect('photo:photo_detail', article_id)