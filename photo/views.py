from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import Photo_PostForm
from .models import Photo_post
from django.core.paginator import Paginator
# Create your views here.

def photo_list(request):
    page = request.GET.get('page', '1')

    photo = Photo_post.objects.order_by('-create_date')

    paginator = Paginator(photo, 10)
    page_obj = paginator.get_page(page)

    context = {'photo': page_obj, 'page': page}
    return render(request, 'photo/photo_list.html', context)


def photo_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload = Photo_post(
            user_id=request.user.id,
            content=content,
            imgfile=img,
        )
        fileupload.save()
        return redirect('photo:photo_list')
    else:
        form = Photo_PostForm()
        return render(request, 'photo/photo_post.html', {'form': form})

def photo_detail(request, photo_id):
    photo_detail = Photo_post.objects.get(pk=photo_id)
    like_list = photo_detail.likes_user.filter(id=request.user.id)
    context = {'photo_detail': photo_detail, 'like_list': like_list}
    return render(request, 'photo/photo_detail.html', context)

@login_required
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

def delete(request, photo_id):
    post = Photo_post.objects.get(pk=photo_id)
    post.delete()
    return redirect('photo:photo_list')
