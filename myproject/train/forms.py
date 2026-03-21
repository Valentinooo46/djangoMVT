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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Виключаємо поточний об'єкт з вибору для previous_unit та next_unit
        if self.instance and self.instance.pk:
            self.fields['previous_unit'].queryset = self.fields['previous_unit'].queryset.exclude(pk=self.instance.pk)
            self.fields['next_unit'].queryset = self.fields['next_unit'].queryset.exclude(pk=self.instance.pk)

    def clean(self):
        cleaned_data = super().clean()
        previous_unit = cleaned_data.get('previous_unit')
        next_unit = cleaned_data.get('next_unit')

        # Додаткова перевірка на цикли
        if previous_unit and next_unit:
            if previous_unit == next_unit:
                raise forms.ValidationError("Попередня та наступна одиниці не можуть бути однаковими.")

        return cleaned_data

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Виключаємо поточний об'єкт з вибору для previous_unit та next_unit
        if self.instance and self.instance.pk:
            self.fields['previous_unit'].queryset = self.fields['previous_unit'].queryset.exclude(pk=self.instance.pk)
            self.fields['next_unit'].queryset = self.fields['next_unit'].queryset.exclude(pk=self.instance.pk)

    def clean(self):
        cleaned_data = super().clean()
        previous_unit = cleaned_data.get('previous_unit')
        next_unit = cleaned_data.get('next_unit')

        # Додаткова перевірка на цикли
        if previous_unit and next_unit:
            if previous_unit == next_unit:
                raise forms.ValidationError("Попередня та наступна одиниці не можуть бути однаковими.")

        return cleaned_data