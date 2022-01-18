from django.shortcuts import render,redirect
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
        form = Photo_PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.save()
            return redirect('photo:photo_list')
    else:
        form = Photo_PostForm()
        return render(request, 'photo/photo_post.html', {'form': form})