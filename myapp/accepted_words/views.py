from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .form import WordForm
from .utils.get_valid_string import get_accepted_words

# Create your views here.

@login_required
def accept_words(request):
   if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            accepted_word = get_accepted_words(form.cleaned_data['words'])
            return render(request, 'accepted_words/accept_words.html', {'form': form, 'accepted_word': accepted_word})
   else:
        form = WordForm()
   return render(request, 'accepted_words/accept_words.html', {'form': form})

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accept_words')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
