from django.shortcuts import render
from .models import Author
from django.shortcuts import render

# Create your views here.
def authors_list(request):
    creators = Author.objects.all()
    return render(request, 'authors/authors_list.html', {"authors_list": creators})

def author_details(request, pk):
    details = Author.objects.filter(id=pk)
    return render(request, 'authors/author_details.html', {"author_details": details})

