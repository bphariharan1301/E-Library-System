from books.models import Book, Category
from django.shortcuts import render
# from books.forms import SearchForm

# Create your views here.


def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()

    context = {
        'books': books,
        'categories': categories,
    }
    return render(request, 'library/index.html', context)


def about(request):
    return render(request, 'library/about.html')


def contact(request):
    context = {}
    return render(request, 'library/contact.html', context)
