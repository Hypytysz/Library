from django.shortcuts import render

# Create your views here.
from books.models import Book
from authors.models import Author


def books(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {"books": books})

def book(request, pk):
    details = Book.objects.filter(id=pk)
    return render(request, 'books/book.html', {"book": details})
