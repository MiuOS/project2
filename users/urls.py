from django.urls import path
from .views import register_request, login_request, logout_request, ProfileDetailView, edit_profile

urlpatterns = [
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('profile/<slug:username>/', ProfileDetailView.as_view(), name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    # Add other URLs as needed
]