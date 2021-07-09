from django.shortcuts import get_object_or_404, render
from .models import Book
# Create your views here.


def books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book' : book,
    }

    return render(request, 'books/book.html', context)
