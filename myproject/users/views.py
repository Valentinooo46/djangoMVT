
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm

def dec(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@dec
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@dec
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
            except IntegrityError:
                form.add_error("username", "A user with that username already exists.")
            else:
                auth_login(request, user)
                return redirect("train_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("train_list")
        else:
            return render(request, "login.html", {"form": AuthenticationForm(), "error": "Invalid username or password"})
    form = AuthenticationForm()

    # Повертаємо шаблон з формою
    return render(request, "login.html", {"form": form})

def logout_view(request):
    auth_logout(request)
    return redirect("login")
