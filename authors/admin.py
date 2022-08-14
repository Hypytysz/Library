from django.contrib import admin

# Register your models here.
from authors.models import Author

@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']


