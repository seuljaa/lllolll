from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import comment
from noti.models import Noti
from .forms import Photo_PostForm
from .models import Photo_post, Photo_Image
from django.core.paginator import Paginator


# Create your views here.

def photo_list(request):
    page = request.GET.get('page', '1')
    photo = Photo_post.objects.order_by('-create_date')
    img = []
    for photo_id in photo:
        img.append(Photo_Image.objects.filter(post_id=photo_id).first())

    paginator = Paginator(photo, 10)
    page_obj = paginator.get_page(page)

    context = {'photo': page_obj, 'page': page, 'img': img}
    return render(request, 'photo/photo_list.html', context)


@login_required(login_url='accounts:sign_in')
def photo_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        img_list = request.FILES.getlist('imgfile[]')
        images = Photo_post.objects.create(user_id=request.user.id, content=content)
        images.save()
        for img in img_list:
            Photo_Image.objects.create(post=Photo_post.objects.last(), imgfile=img)
        return redirect('photo:photo_list')
    else:
        form = Photo_PostForm()
    return render(request, 'photo/photo_post.html', {'form': form})


@login_required(login_url='accounts:sign_in')
def photo_detail(request, photo_id):
    photo_detail = Photo_post.objects.get(pk=photo_id)
    photo = Photo_Image.objects.filter(post_id=photo_id)
    like_list = photo_detail.likes_user.filter(id=request.user.id)
    context = {'photo_detail': photo_detail, 'like_list': like_list, 'photo':photo}
    return render(request, 'photo/photo_detail.html', context)


@login_required(login_url='accounts:sign_in')
def photo_like(request, photo_id):
    post = get_object_or_404(Photo_post, id=photo_id)
    user = request.user

    if post.likes_user.filter(id=user.id).exists():
        post.likes_user.remove(user)
        post.like_count -= 1
        post.save()

    else:
        post.likes_user.add(user)
        post.like_count += 1
        post.save()
    return redirect('photo:photo_detail', photo_id)


@login_required(login_url='accounts:sign_in')
def delete(request, photo_id):
    post = Photo_post.objects.get(pk=photo_id)
    if request.user != post.user:
        messages.error(request, '본인이 게시글만 삭제할수있습니다.')
        return redirect('photo:photo_detail', photo_id)
    else:
        post.delete()
        return redirect('photo:photo_list')
