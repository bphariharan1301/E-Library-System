
from .models import Book
from .choice import category_choices
from django import forms


class SearchForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = ('name', 'author', 'category')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Book Name', 'class': 'text-input name-input'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author Name', 'class': 'text-input subject-input'}),
            'category': forms.Select(choices=category_choices, attrs={'class': 'text-input subject-input'}),
        }
