from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Movie, Actor, Director, Genre
from .forms import MovieFilterForm, SearchForm


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    paginate_by = 12
    context_object_name = 'movies'
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        form = MovieFilterForm(self.request.GET)
        
        if form.is_valid():
            if form.cleaned_data.get('title'):
                queryset = queryset.filter(title__icontains=form.cleaned_data['title'])
                
            if form.cleaned_data.get('genre'):
                queryset = queryset.filter(genres=form.cleaned_data['genre'])
        
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = MovieFilterForm(self.request.GET or None)
        context['search_form'] = SearchForm(self.request.GET or None)
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        context['related_movies'] = Movie.objects.filter(
            genres__in=movie.genres.all()
        ).exclude(id=movie.id).distinct()[:4]
        return context


def search_view(request):
    search_form = SearchForm(request.GET or None)
    movies = Movie.objects.none()
    
    if search_form.is_valid() and search_form.cleaned_data['query']:
        query = search_form.cleaned_data['query']
        movies = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(actors__name__icontains=query) |
            Q(director__name__icontains=query) |
            Q(genres__name__icontains=query)
        ).distinct()
    
    return render(request, 'search_results.html', {
        'movies': movies,
        'search_form': search_form,
    })