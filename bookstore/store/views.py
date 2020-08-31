from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'store/index.html')


def get_category(request):
    return render(request, 'store/category.html')