from django.shortcuts import render
from .models import Book
# Create your views here.


def books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)
