from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import DealItems

# Create your views here.

def main(request):
    return render(request, 'main.html')

def deal_list(request):
    page = request.GET.get('page', '1')
    search_keyword = request.GET.get('search_keyword', '')

    deal_items = DealItems.objects.order_by('-reg_date')
    paginator = Paginator(deal_items, 10)
    page_obj = paginator.get_page(page)

    context = {'deal_items': page_obj, 'page': page}
    return render(request, 'deal/deal_list.html', context)