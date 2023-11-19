from django.urls import path
from .views import MoviesListView, MovieDetailView, CategoryListView, add_review, favourite_toggle, watch_later_toggle, add_to_history

urlpatterns = [
    path('', MoviesListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('categories', CategoryListView.as_view(), name='category_list'),
    path('movies/category/<str:category>/', MoviesListView.as_view(), name='movies_by_category'),
    path('<int:movie_id>/review', add_review, name='add_review'),
    path('<int:movie_id>/favourite', favourite_toggle, name='favourite_toggle'),
    path('<int:movie_id>/watch_later', watch_later_toggle, name='watch_later_toggle'),
    path('<int:movie_id>/add_to_history', add_to_history, name='add_to_history'),
]