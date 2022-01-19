from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
import json

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
    return render(request, 'photo/photo_detail.html', {'photo_detail': photo_detail})

@login_required
@require_POST
def photo_like(request):
    pk = request.POST.get('pk', None)
    photo = get_object_or_404(Photo_post, pk=pk)
    user = request.user

    if photo.likes_user.filter(id=user.id).exists():
        photo.likes_user.remove(user)
    else:
        photo.likes_user.add(user)

    context = {'likes_count':photo.count_likes_user()}
    return HttpResponse(json.dumps(context), content_type="application/json")