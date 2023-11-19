from django.urls import path
from .views import MoviesListView, MovieDetailView, CategoryListView, add_review

urlpatterns = [
    path('', MoviesListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('categories', CategoryListView.as_view(), name='category_list'),
    path('movies/category/<str:category>/', MoviesListView.as_view(), name='movies_by_category'),
    path('<int:movie_id>/review', add_review, name='add_review'),
]