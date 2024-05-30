from django.shortcuts import render
from .models import Book


def index(request):
    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, 'index.html', context)