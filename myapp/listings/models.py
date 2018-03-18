from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class MovieList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

class SongList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

class BookList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    book_author = models.CharField(max_length=100, blank=True, null=True)
