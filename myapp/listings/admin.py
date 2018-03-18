from django.contrib import admin
from .models import MovieList, SongList, BookList

admin.site.register(MovieList)
admin.site.register(SongList)
admin.site.register(BookList)
# Register your models here.
