from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView

from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                # Invalid login
                pass
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})

@login_required(login_url="login")
def logout_request(request):
    logout(request)
    return redirect("home")

class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = "users/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
