from books.forms import SearchForm
from django.shortcuts import get_object_or_404, render
from .models import Book
from .choice import category_choices
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
        'book': book,
    }

    return render(request, 'books/book.html', context)


def search(request):
    books = Book.objects.all()

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            books = books.filter(name__iexact=name)

    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            books = books.filter(author__iexact=author)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            books = books.filter(category__iexact=category)
    print(books)
    context = {
        'category_choices': category_choices,
        'books': books,
        'values': request.GET,
        # 'list1': list1,
    }

    return render(request, 'books/search.html', context)
