from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from movies.models import Movie


# Create your views here.

class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        return Movie.objects.all().order_by('-added')

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'