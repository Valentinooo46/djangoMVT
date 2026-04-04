from django.shortcuts import render, redirect
from .models import Train, Carriage
from .forms import TrainForm, CarriageForm
from django.contrib.auth.decorators import login_required

# TRAIN CRUD
@login_required(login_url="/login/")
def train_list(request):
    trains = Train.objects.all()
    return render(request, "train_list.html", {"trains": trains})

@login_required(login_url="/login/")
def train_detail(request, pk):
    train = Train.objects.get(pk=pk)
    chain_units = train.get_previous_units_chain() + [train] + train.get_next_units_chain()
    units_with_type = []
    for unit in chain_units:
        if hasattr(unit, "train"):
            unit_type = 'train'
        elif hasattr(unit, "carriage"):
            unit_type = 'carriage'
        else:
            unit_type = 'unknown'
        units_with_type.append((unit, unit_type))


    return render(request, "train_detail.html", {"train": train, "units_with_type": units_with_type})

@login_required(login_url="/login/")
def create_train(request):
    if request.method == "POST":
        form = TrainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("train_list")
    else:
        form = TrainForm()
    return render(request, "create_train.html", {"form": form})

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def delete_train(request, pk):
    train = Train.objects.get(pk=pk)
    if request.method == "POST":
        train.delete()
        return redirect("train_list")
    return render(request, "delete_train.html", {"train": train})

# CARRIAGE CRUD
@login_required(login_url="/login/")
def carriage_list(request):
    carriages = Carriage.objects.all()
    return render(request, "carriage_list.html", {"carriages": carriages})

@login_required(login_url="/login/")
def carriage_detail(request, pk):
    carriage = Carriage.objects.get(pk=pk)
    chain_units = carriage.get_previous_units_chain() + [carriage] + carriage.get_next_units_chain()
    units_with_type = []
    for unit in chain_units:
        if hasattr(unit, "train"):
            unit_type = 'train'
        elif hasattr(unit, "carriage"):
            unit_type = 'carriage'
        else:
            unit_type = 'unknown'
        units_with_type.append((unit, unit_type))
    return render(request, "carriage_detail.html", {"carriage": carriage, "units_with_type": units_with_type})

@login_required(login_url="/login/")
def create_carriage(request):
    if request.method == "POST":
        form = CarriageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("carriage_list")
    else:
        form = CarriageForm()
    return render(request, "create_carriage.html", {"form": form})

@login_required(login_url="/login/")
def update_carriage(request, pk):
    carriage = Carriage.objects.get(pk=pk)
    if request.method == "POST":
        form = CarriageForm(request.POST,request.FILES, instance=carriage)
        if form.is_valid():
            form.save()
            return redirect("carriage_list")
    else:
        form = CarriageForm(instance=carriage)
    return render(request, "update_carriage.html", {"form": form})

@login_required(login_url="/login/")
def delete_carriage(request, pk):
    carriage = Carriage.objects.get(pk=pk)
    if request.method == "POST":
        carriage.delete()
        return redirect("carriage_list")
    return render(request, "delete_carriage.html", {"carriage": carriage})