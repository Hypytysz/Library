from django.contrib import admin

# Register your models here.
from .models import CommentPost

@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    pass
