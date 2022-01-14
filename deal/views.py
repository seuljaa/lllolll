from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import DealItems
from .forms import PostForm

# Create your views here.

def main(request):
    return render(request, 'main.html')

def deal_list(request):
    deal_items = DealItems.objects.order_by('-create_date')
    context = {'deal_items': deal_items}
    return render(request, 'deal/deal_items_list.html', context)

def post_Armor(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.subject = request.POST.get('subject')
            post.server = request.POST.get('server')
            post.group = request.POST.get('group')
            post.part = request.POST.get('part')
            post.price = request.POST.get('price')
            post.price_kind = request.POST.get('price_kind')
            post.star_force = request.POST.get('star_force')
            post.ability_1 = request.POST.get('ability_1')
            post.ability_2 = request.POST.get('ability_2')
            post.sale_buy = request.POST.get('sale_buy')
            post.save()
            return redirect('main')
    else :
        form = PostForm()
    return render(request, 'deal/deal_item_post.html', {'form':form} )