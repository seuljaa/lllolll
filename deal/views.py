from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import DealItems, Group
from .forms import PostForm, Group_Armor
from django.contrib import messages


# Create your views here.

class Exception(Exception):
    pass


def main(request):
    return render(request, 'main.html')

def deal_list(request):
    page = request.GET.get('page', '1')
    search_keyword = request.GET.get('search_keyword', '')
    filter_group = request.GET.getlist('group')
    filter_part = request.GET.getlist('part')
    filter_star_force = request.GET.getlist('star_force')
    filter_ability_1 = request.GET.getlist('ability_1')
    filter_ability_2 = request.GET.getlist('ability_2')

    deal_items = DealItems.objects.filter(category=True).order_by('-create_date')

    if search_keyword:
        deal_items = deal_items.filter(
            Q(subject__icontains=search_keyword)
        ).distinct()

    if filter_group:
        query = Q()
        for i in filter_group:
            query = query | Q(group__icontains=i)
            deal_items = deal_items.filter(query)

    if filter_part:
        query = Q()
        for i in filter_part:
            query = query | Q(part__icontains=i)
            deal_items = deal_items.filter(query)

    if filter_star_force:
        query = Q()
        for i in filter_star_force:
            query = query | Q(star_force__icontains=i)
            deal_items = deal_items.filter(query)

    if filter_ability_1:
        query = Q()
        for i in filter_ability_1:
            query = query | Q(ability_1__icontains=i)
            deal_items = deal_items.filter(query)

    if filter_ability_2:
        query = Q()
        for i in filter_ability_2:
            query = query | Q(ability_2__icontains=i)
            deal_items = deal_items.filter(query)

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
            post.category = True
            post.server = request.user.server
            post.group = request.POST.get('group')
            post.kind = request.POST.get('kind')
            post.part = request.POST.get('choose')
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
        grou_armor = Group_Armor()

    return render(request, 'deal/deal_item_post.html', {'form': form, 'grou_armor':grou_armor})

def post_gita(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.subject = request.POST.get('subject')
            post.category = False
            post.server = request.user.server
            post.kind = request.POST.get('kind')
            post.price = request.POST.get('price')
            post.sale_buy = request.POST.get('sale_buy')
            post.save()
            return redirect('deal:deal_gita_list')
    else:
        form = PostForm()
        grou_armor = Group_Armor()

    return render(request, 'deal/deal_gita_post.html', {'form': form, 'grou_armor':grou_armor})

@login_required(login_url='accounts:sign_in')
def deal_detail(request, deal_id):
    detail = DealItems.objects.get(pk=deal_id)
    return render(request, 'deal/deal_items_detail.html', {'detail':detail})

@login_required(login_url='accounts:sign_in')
def deal_gita_detail(request, deal_id):
    detail = DealItems.objects.get(pk=deal_id)
    return render(request, 'deal/deal_gita_detail.html', {'detail':detail})


def deal_gita_list(request):
    page = request.GET.get('page', '1')
    search_keyword = request.GET.get('search_keyword', '')
    filter_kind = request.GET.getlist('kind')

    deal_items = DealItems.objects.filter(category=False).order_by('-create_date')

    if search_keyword:
        deal_items = deal_items.filter(
            Q(subject__icontains=search_keyword)
        ).distinct()

    if filter_kind:
        query = Q()
        for i in filter_kind:
            query = query | Q(kind__icontains=i)
            deal_items = deal_items.filter(query)

    paginator = Paginator(deal_items, 10)
    page_obj = paginator.get_page(page)

    context = {'deal_items': page_obj, 'page': page, 'search_keyword': search_keyword}
    return render(request, 'deal/deal_gita_list.html', context)

