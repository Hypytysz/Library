from django.contrib import admin
from books.models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author_first_name', 'author_last_name']

    def author_first_name(self, obj):
        return obj.author.first_name

    def author_last_name(self, obj):
        return obj.author.last_name

    author_first_name.admin_order_field = 'author__first_name'
    author_last_name.admin_order_field = 'author__last_name'