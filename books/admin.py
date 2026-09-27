from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_published', 'is_available')

admin.site.register(Book, BookAdmin)