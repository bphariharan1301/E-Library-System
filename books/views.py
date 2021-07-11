from books.forms import SearchForm
from django.shortcuts import get_object_or_404, render
from .models import Book, Category
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
    queryset_list = Book.objects.order_by('-book_date')

    cats = Category.objects.all()

    # Book Name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)

    # Author Name
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(author__iexact=author)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    context = {
        'books': queryset_list,
        'cats': cats,
        'values': request.GET
    }

    return render(request, 'books/search.html', context)
