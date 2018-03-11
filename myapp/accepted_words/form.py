from django import forms

class WordForm(forms.Form):
    words = forms.CharField(max_length=100)

