from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='person_photos/', blank=True, null=True)
    bio = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Actor(Person):
    pass


class Director(Person):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='directed_movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    released = models.BooleanField(default=True)
    release_year = models.PositiveIntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_year', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
