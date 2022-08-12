from django.shortcuts import render

# Create your views here.
from books.models import Book


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {"books_list": books})

def book_details(request, pk):
    details = Book.objects.filter(id=pk)
    return render(request, 'books/book_details.html', {"book_details": details})