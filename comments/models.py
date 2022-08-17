from django.db import models

# Create your models here.

class CommentPost(models.Model):
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')