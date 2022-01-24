from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import DealItems
from .forms import PostForm


# Create your views here.

def main(request):
    return render(request, 'main.html')

def deal_list(request):
    page = request.GET.get('page', '1')
    search_keyword = request.GET.get('search_keyword', '')

    deal_items = DealItems.objects.order_by('-create_date')

    if search_keyword:
        deal_items = deal_items.filter(
            Q(subject__icontains=search_keyword)
        ).distinct()

    paginator = Paginator(deal_items, 10)
    page_obj = paginator.get_page(page)

    context = {'deal_items': page_obj, 'page': page, 'search_keyword': search_keyword}
    return render(request, 'deal/deal_items_list.html', context)

@login_required(login_url='accounts:sign_in')
def post_Armor(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.subject = request.POST.get('subject')
            post.server = request.user.server
            post.group = request.POST.get('group')
            post.part = request.POST.get('part')
            post.price = request.POST.get('price')
            post.price_kind = request.POST.get('price_kind')
            post.star_force = request.POST.get('star_force')
            post.ability_1 = request.POST.get('ability_1')
            post.ability_2 = request.POST.get('ability_2')
            post.sale_buy = request.POST.get('sale_buy')
            post.save()
            return redirect('deal:deal_list')
    else:
        form = PostForm()
    return render(request, 'deal/deal_item_post.html', {'form': form})

@login_required(login_url='accounts:sign_in')
def deal_detail(request, deal_id):
    detail = DealItems.objects.get(pk=deal_id)
    return render(request, 'deal/deal_items_detail.html', {'detail':detail})


