from django import forms
from .models import *
from django.forms.widgets import Textarea, TextInput

class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name', 'description', 'image']
        widgets = {
            "name": TextInput(attrs={"class": "input"}),
            "description": Textarea(attrs={"rows": 5, "class": "textarea"})
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['type', 'name', 'image', 'price_per_hour', 'price_per_day', 'insurance'
                  , 'seat', 'description', 'employee', 'vehicle_status']
        widgets = {
            "name": TextInput(attrs={"class": "input"}),
            "description": Textarea(attrs={"rows": 5, "class": "textarea"}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'position']



