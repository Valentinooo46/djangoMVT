from django import forms
from .models import Train, Carriage
from PIL import Image

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
            self.fields['previous_unit'].queryset = self.instance.get_available_previous_units()
            self.fields['next_unit'].queryset = self.instance.get_available_next_units()

    def save(self, commit=True):
        instance = super().save(commit=False)

        if instance.image:
            img = Image.open(instance.image)
           
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) // 2
            top = (height - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim
            img = img.crop((left, top, right, bottom))

            
            img.save(instance.image.path)

        if commit:
            instance.save()
        return instance


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
        fields = ["name", "number", "previous_unit", "next_unit","image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "previous_unit": forms.Select(attrs={"class": "form-control"}),
            "next_unit": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Виключаємо поточний об'єкт з вибору для previous_unit та next_unit
        if self.instance and self.instance.pk:
            self.fields['previous_unit'].queryset = self.instance.get_available_previous_units()
            self.fields['next_unit'].queryset = self.instance.get_available_next_units()

    def save(self, commit=True):
        instance = super().save(commit=False)

        if instance.image:
            img = Image.open(instance.image)
            
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) // 2
            top = (height - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim
            img = img.crop((left, top, right, bottom))

          
            img.save(instance.image.path)

        if commit:
            instance.save()
        return instance

    def clean(self):
        cleaned_data = super().clean()
        previous_unit = cleaned_data.get('previous_unit')
        next_unit = cleaned_data.get('next_unit')

        # Додаткова перевірка на цикли
        if previous_unit and next_unit:
            if previous_unit == next_unit:
                raise forms.ValidationError("Попередня та наступна одиниці не можуть бути однаковими.")

        return cleaned_data