
from django.contrib.auth import login

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("train_list")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form}) 