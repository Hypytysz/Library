from django.contrib import admin

# Register your models here.
from authors.models import Author, Bio


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ['author', 'bio_excerpt']

    def bio_excerpt(self, obj):
        return f'{obj.bio[:30]} ...'
