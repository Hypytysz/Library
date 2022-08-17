from django.shortcuts import render, redirect

# Create your views here.
from comments.forms import CommentForm
from posts.forms import PostForm
from posts.models import Post


def posts(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    return render(request, 'posts/posts.html', {"posts":posts, 'post_form': PostForm()})

def post_details(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

    comment_form = CommentForm()
    data = {'title': post.title, 'content': post.content, 'author':post.author}
    return render(request, 'posts/details.html', {"post":post, 'comment_form': comment_form})

def post_edit(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("posts")
    return render(request, 'posts/edit.html', {"post":post})

def delete_post(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect("posts")

