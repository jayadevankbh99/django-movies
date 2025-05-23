from django.contrib import admin

from django.contrib import admin
from .models import Actor, Director, Genre, Movie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'rating')
    list_filter = ('release_year', 'genres', 'director')
    search_fields = ('title', 'description')
    filter_horizontal = ('actors', 'genres')
    fieldsets = (
        (None, {
            'fields': ('title', 'director','released', 'release_year', 'description', 'poster', 'rating')
        }),
        ('Categories', {
            'fields': ('actors', 'genres')
        }),
    )
