from django import forms
from .models import *
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime


class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name', 'description', 'image']
        widgets = {
            "name": TextInput(attrs={"class": "input"}),
            "description": Textarea(attrs={"rows": 3, "class": "textarea"})
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['type', 'name', 'image', 'price_per_hour', 'price_per_day', 'insurance'
                  , 'seat', 'description', 'employee', 'vehicle_status', 'number']
        widgets = {
            "name": TextInput(attrs={"class": "input"}),
            "number": TextInput(attrs={"class": "input"}),
            "description": Textarea(attrs={"rows": 3, "class": "textarea"}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'position']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            "username": TextInput(attrs={"class": "input"}),
            "email": TextInput(attrs={"class": "input"}),
            "first_name": TextInput(attrs={"class": "input"}),
            "last_name": TextInput(attrs={"class": "input"}),
        }

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    

class RentFormDay(forms.ModelForm):
    
    class Meta:
        model = Rent
        fields = ['start_time', 'end_time']
        widgets = {
            "start_time": SelectDateWidget(),
            "end_time": SelectDateWidget()
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_time")
        end_date = cleaned_data.get("end_time")
        now = datetime.now()

        if end_date < start_date:
            self.add_error(
                "start_date",
                "Due date cannot be before start date"
            )
        return cleaned_data

class RentFormHour(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['start_time', 'end_time']
        widgets = {
            "start_time": SelectDateWidget(),
            "end_time": SelectDateWidget()
        }




