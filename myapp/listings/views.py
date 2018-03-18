from django.shortcuts import render, redirect, get_object_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MovieList, SongList, BookList
from .forms import MovieForm, FilterSearchForm, SongForm, BookForm

@login_required
def movie_list(request):
    if request.method == "POST":
        form = FilterSearchForm(request.POST)
        if form.is_valid():
            listings = MovieList.objects.filter(movie__contains=form.cleaned_data['filter_word'])
    else:
        form = FilterSearchForm()
        listings = MovieList.objects.all()
    return render(request, 'listings/movie_list.html', {'listings': listings, 'form': form, 'list_type' : 'Movie'})

@login_required
def song_list(request):
    if request.method == "POST":
        form = FilterSearchForm(request.POST)
        if form.is_valid():
            listings = SongList.objects.filter(song__contains=form.cleaned_data['filter_word'])
    else:
        form = FilterSearchForm()
        listings = SongList.objects.all()
    return render(request, 'listings/song_list.html', {'form': form, 'listings' : listings}) 

@login_required
def add_data(request, list_type):
    lists = {'book' : BookForm, 'movie' : MovieForm, 'song' : SongForm}
    form_type = lists[list_type]
    if request.method == "POST":
        form = form_type(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.author_id = request.user.id
            data.save()
            return redirect('{}_list'.format(list_type))
    else:
        form = form_type()
    return render(request, 'listings/edit_list.html', {'form': form, 'list_type': list_type} ) 

@login_required
def edit_data(request, pk, list_type):
    lists = {'book' : BookForm, 'movie' : MovieForm, 'song' : SongForm}
    lists_model = {'book' : BookList, 'movie' : MovieList, 'song' : SongList}
    form_type = lists[list_type]
    model_type = lists_model[list_type]

    song = get_object_or_404(model_type, pk=pk)

    if request.method == "POST":
        form = form_type(request.POST, instance=song)
        if form.is_valid():
            data = form.save(commit=False)
            data.author_id = request.user.id
            data.save()
            return redirect('{}_list'.format(list_type))
    else:
        form = form_type(instance=song)
    return render(request, 'listings/edit_list.html', {'form': form, 'list_type' : list_type}) 

@login_required
def book_list(request):
    if request.method == "POST":
        form = FilterSearchForm(request.POST)
        if form.is_valid():
            listings = BookList.objects.filter(book__contains=form.cleaned_data['filter_word'])
    else:
        form = FilterSearchForm()
        listings = BookList.objects.all()
    return render(request, 'listings/book_list.html', {'form': form, 'listings' : listings}) 


@login_required
def remove_list(request, pk, list_type):
    lists = {'book' : BookList, 'movie' : MovieList, 'song' : SongList}
    data = get_object_or_404(lists[list_type], pk=pk)
    data.delete()
    return redirect('{}_list'.format(list_type))

# Create your views here.
