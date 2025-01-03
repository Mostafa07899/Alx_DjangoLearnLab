from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in list view
    search_fields = ('title', 'author')  # Enable search
    list_filter = ('publication_year',)  # Enable filtering

admin.site.register(Book, BookAdmin)
