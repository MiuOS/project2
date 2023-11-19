from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from movies.models import Movie, Category, Review
from .forms import ReviewForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(movie=self.object)
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'movies/category_list.html'
    context_object_name = 'categories'

def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review()
            review.movie = movie
            review.user = request.user
            review.text = form.cleaned_data['text']
            review.rating = form.cleaned_data['rating']
            review.save()
            return redirect('movie_detail', pk=movie_id)
        else:
            return render(request, 'movies/add_review.html', {'form': form, 'movie': movie})
    else:
        form = ReviewForm()
    return render(request, 'movies/add_review.html', {'form': form, 'movie': movie})