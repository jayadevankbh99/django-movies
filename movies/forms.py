from django import forms
from .models import Movie, Actor, Director, Genre


class MovieFilterForm(forms.Form):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by title...'}))
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        empty_label="Any Genre",
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search movies...', 'class': 'form-control'})
    )