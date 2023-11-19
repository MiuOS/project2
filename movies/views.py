from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from movies.models import Movie, Category


# Create your views here.

class MoviesListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        category_name = self.kwargs.get('category', None)
        queryset = Movie.objects.all().order_by('-added')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)
        return queryset

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class CategoryListView(ListView):
    model = Category
    template_name = 'movies/category_list.html'
    context_object_name = 'categories'