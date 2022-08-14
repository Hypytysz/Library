from django.shortcuts import render
from .models import Author
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {'homepage':{}})
def authors_list(request):
    creators = Author.objects.all()
    return render(request, 'authors/authors_list.html', {"authors_list": creators})

def author_details(request, pk):
    details = Author.objects.filter(id=pk)
    details2 = Author.objects.get(pk=pk)
    books = details2.books.all()
    return render(request, 'authors/author_details.html', {"author_details": details, 'author_books': books})


