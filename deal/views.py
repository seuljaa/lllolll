from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import DealItems

# Create your views here.

def main(request):
    return render(request, 'main.html')
