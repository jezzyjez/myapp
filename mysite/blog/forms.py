from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class FilterSearch(forms.form)
    words = form.CharField(max_length=100)
