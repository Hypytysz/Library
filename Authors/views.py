from django.shortcuts import render

# Create your views here.
def authors_list(request):
    return render(request, 'blog/authors_list.html', {})