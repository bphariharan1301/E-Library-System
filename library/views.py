from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'library/index.html', context)

def books(request):
    context = {}
    return render(request, 'library/books.html', context)
