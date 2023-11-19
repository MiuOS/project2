from django.shortcuts import render
from django.views.generic import ListView

from movies.models import Movie


# Create your views here.

class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        return Movie.objects.all().order_by('-added')