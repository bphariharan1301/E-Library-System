from books.models import Book
from django.shortcuts import render

# Create your views here.


def home(request):
    book = Book.objects.all()

    context = {
        'book': book,
    }
    return render(request, 'library/index.html', context)


def about(request):
    context = {}
    return render(request, 'library/about.html', context)


def contact(request):
    context = {}
    return render(request, 'library/contact.html', context)
