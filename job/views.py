from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Post_job

def job_list(request):
    page = request.GET.get('page', '1')
    search_keyword = request.GET.get('search_keyword', '')

    post_job_list = Post_job.objects.order_by('-create_date')

    if search_keyword:
        post_job_list = Post_job.filter(
            Q(subject__icontains=search_keyword)
        ).distinct()

    paginator = Paginator(post_job_list, 10)
    page_obj = paginator.get_page(page)

    context = {'job': page_obj, 'page': page, 'search_keyword': search_keyword}
    return render(request, 'job/job_list.html', context)