from django.shortcuts import render
from .models import Author
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {'homepage':{}})

def authors_list(request):
    creators = Author.objects.all()
    return render(request, 'authors/authors.html', {"authors": creators})

def author_details(request, pk):
    details = Author.objects.filter(id=pk)
    author = Author.objects.get(pk=pk)
    books = author.books.all()
    return render(request, 'authors/author.html', {"author": author, 'author_books': books})


