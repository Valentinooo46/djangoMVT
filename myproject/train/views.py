from django.shortcuts import render, redirect
from .models import Train, Carriage
from .forms import TrainForm, CarriageForm
from django.contrib.auth.decorators import login_required

# TRAIN CRUD
@login_required(login_url="/register/")
def train_list(request):
    trains = Train.objects.all()
    return render(request, "train_list.html", {"trains": trains})

@login_required(login_url="/register/")
def train_detail(request, pk):
    train = Train.objects.get(pk=pk)
    return render(request, "train_detail.html", {"train": train})

@login_required(login_url="/register/")
def create_train(request):
    if request.method == "POST":
        form = TrainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("train_list")
    else:
        form = TrainForm()
    return render(request, "create_train.html", {"form": form})

@login_required(login_url="/register/")
def update_train(request, pk):
    train = Train.objects.get(pk=pk)
    if request.method == "POST":
        form = TrainForm(request.POST, request.FILES, instance=train)
        if form.is_valid():
            form.save()
            return redirect("train_list")
    else:
        form = TrainForm(instance=train)
    return render(request, "update_train.html", {"form": form})

@login_required(login_url="/register/")
def delete_train(request, pk):
    train = Train.objects.get(pk=pk)
    if request.method == "POST":
        train.delete()
        return redirect("train_list")
    return render(request, "delete_train.html", {"train": train})

# CARRIAGE CRUD
@login_required(login_url="/register/")
def carriage_list(request):
    carriages = Carriage.objects.all()
    return render(request, "carriage_list.html", {"carriages": carriages})

@login_required(login_url="/register/")
def carriage_detail(request, pk):
    carriage = Carriage.objects.get(pk=pk)
    return render(request, "carriage_detail.html", {"carriage": carriage})

@login_required(login_url="/register/")
def create_carriage(request):
    if request.method == "POST":
        form = CarriageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("carriage_list")
    else:
        form = CarriageForm()
    return render(request, "create_carriage.html", {"form": form})

@login_required(login_url="/register/")
def update_carriage(request, pk):
    carriage = Carriage.objects.get(pk=pk)
    if request.method == "POST":
        form = CarriageForm(request.POST, instance=carriage)
        if form.is_valid():
            form.save()
            return redirect("carriage_list")
    else:
        form = CarriageForm(instance=carriage)
    return render(request, "update_carriage.html", {"form": form})

@login_required(login_url="/register/")
def delete_carriage(request, pk):
    carriage = Carriage.objects.get(pk=pk)
    if request.method == "POST":
        carriage.delete()
        return redirect("carriage_list")
    return render(request, "delete_carriage.html", {"carriage": carriage})