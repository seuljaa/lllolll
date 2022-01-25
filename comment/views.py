from django.shortcuts import render,redirect
from .models import Comment
from photo.models import Photo_post
from deal.models import DealItems
from job.models import Post_job
# Create your views here.


def comment_photo(request, photo_id):
    post = Photo_post.objects.get(pk=photo_id)
    if request.method == 'POST':
        comment = Comment(user=request.user, content=request.POST.get('comment'), photo_post=post)
        comment.save()
        return redirect('photo:photo_detail', photo_id=photo_id)

def comment_deal(request, deal_id):
    post = DealItems.objects.get(pk=deal_id)
    if request.method == 'POST':
        comment = Comment(user=request.user, content=request.POST.get('comment'), deal_items=post)
        comment.save()
        return redirect('deal:deal_detail', deal_id=deal_id)

def comment_job(request, job_id):
    post = Post_job.objects.get(pk=job_id)
    if request.method == 'POST':
        comment = Comment(user=request.user, content=request.POST.get('comment'), job_post=post)
        comment.save()
        return redirect('job:job_detail', post_id=job_id)