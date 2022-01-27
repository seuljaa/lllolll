from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForm
from .models import Post_job


def job_list(request):
    page = request.GET.get('page', '1')
    search_keyword = request.GET.get('search_keyword', '')
    filter_boss = request.GET.getlist('boss')
    filter_level = request.GET.getlist('level')

    post_job_list = Post_job.objects.order_by('-create_date')

    if search_keyword:
        post_job_list = post_job_list.filter(
            Q(subject__icontains=search_keyword)
        ).distinct()

    if filter_boss:
        query = Q()
        for i in filter_boss:
            query = query | Q(boss__icontains=i)
            post_job_list = post_job_list.filter(query)

    if filter_level:
        query = Q()
        for i in filter_level:
            query = query | Q(level__icontains=i)
            post_job_list = post_job_list.filter(query)

    paginator = Paginator(post_job_list, 10)
    page_obj = paginator.get_page(page)

    context = {'job': page_obj, 'page': page, 'search_keyword': search_keyword}
    return render(request, 'job/job_list.html', context)


@login_required(login_url='accounts:sign_in')
def post_job(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.subject = request.POST.get('subject')
            post.kind = request.POST.get('kind')
            post.server = request.user.server
            post.boss = request.POST.get('boss')
            post.level = request.POST.get('level')
            post.total = request.POST.get('total')
            post.job = request.POST.get('job')
            post.save()
            return redirect('job:job_list')
    else:
        form = PostForm()

    return render(request, 'job/job_post.html', {'form': form})


@login_required(login_url='accounts:sign_in')
def job_detail(request, post_id):
    detail = Post_job.objects.get(pk=post_id)
    return render(request, 'job/job_detail.html', {'detail': detail})
