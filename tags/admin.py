from django.contrib import admin

# Register your models here.
from tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass