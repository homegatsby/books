from django.shortcuts import render
from django.http import HttpResponse
from store.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "store/index.html", {"books": books})


def get_category(request, slug):
    return render(request, 'store/category.html')
