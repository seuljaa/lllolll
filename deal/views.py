from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return render(request, 'main.html')

def deal_list(request):
    return HttpResponse('하이')