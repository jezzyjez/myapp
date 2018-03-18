from django import forms
from .models import MovieList, SongList, BookList

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ('movie', 'release_date', 'genre',)

class SongForm(forms.ModelForm):
    class Meta:
        model = SongList
        fields = ('song', 'release_date', 'genre',)

class BookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ('book', 'release_date', 'book_author',)

class FilterSearchForm(forms.Form):
    filter_word = forms.CharField(max_length=100, required=False)

