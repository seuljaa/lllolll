from django.shortcuts import render,redirect
from .models import Comment
from photo.models import Photo_post
# Create your views here.


def comment_photo(request, photo_id):
    post = Photo_post.objects.get(pk=photo_id)
    if request.method == 'POST':
        comment = Comment(user=request.user, content=request.POST.get('comment'), photo_post=post)
        comment.save()
        return redirect('photo:photo_detail', photo_id=photo_id)