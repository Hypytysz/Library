from django.shortcuts import render, redirect

# Create your views here.
from comments.forms import CommentForm
from comments.models import CommentPost
from posts.forms import PostForm
from posts.models import Post


def posts(request):
    posts = Post.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
    return render(request, 'posts/posts.html', {"posts":posts})

def post_details(request, pk):
    post= Post.objects.get(pk=pk)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = dict(comment_form.cleaned_data)
            data['post'] = post
            comment = CommentPost.objects.create(**data)
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # author = request.POST.get("author")
        # post.title = title
        # post.content = content
        # post.author = author
    comment_form = CommentForm()
    data = {'title': post.title, 'content': post.content, 'author':post.author}
    return render(request, 'posts/details.html', {"post":post, 'comment_form': comment_form})

def post_edit(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post.title = title
        post.content = content
        post.save()
        return redirect("posts")
    return render(request, 'posts/edit.html', {"post":post})

def delete_post(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect("posts")

