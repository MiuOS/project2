from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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
        next_page = request.POST.get('next', '')
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next_page:
                    return redirect(next_page)
                return redirect("home")
            else:
                # Invalid login
                pass
    else:
        next_page = request.GET.get('next', '')
        form = LoginForm(request)
    return render(request, "users/login.html", {"form": form, 'next': next_page})

@login_required(login_url="login")
def logout_request(request):
    logout(request)
    return redirect("home")

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    login_url = "login"

    def get_object(self, queryset=None):
        # Pobranie obiektu użytkownika, tak jak robi to domyślna implementacja
        obj = super().get_object(queryset=queryset)

        # Sprawdzenie, czy zalogowany użytkownik jest właścicielem profilu
        if obj != self.request.user:
            raise Http404("Nie masz uprawnień do przeglądania tego profilu.")

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
