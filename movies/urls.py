from django.urls import path
from .views import MoviesListView, MovieDetailView

urlpatterns = [
    path('', MoviesListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]