from django import forms
from .models import Train, Carriage

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ["name", "number", "departure", "arrival", "departure_time", "arrival_time", "image", "previous_unit", "next_unit"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "departure": forms.TextInput(attrs={"class": "form-control"}),
            "arrival": forms.TextInput(attrs={"class": "form-control"}),
            "departure_time": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "arrival_time": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "previous_unit": forms.Select(attrs={"class": "form-control"}),
            "next_unit": forms.Select(attrs={"class": "form-control"}),
        }

class CarriageForm(forms.ModelForm):
    class Meta:
        model = Carriage
        fields = ["name", "number", "previous_unit", "next_unit"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "previous_unit": forms.Select(attrs={"class": "form-control"}),
            "next_unit": forms.Select(attrs={"class": "form-control"}),
        }