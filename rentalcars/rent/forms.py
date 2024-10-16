from django import forms
from .models import *
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import make_aware, get_current_timezone
from django.forms import SplitDateTimeField


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
    

class RentForm(forms.ModelForm):
    start_time = SplitDateTimeField(widget=SplitDateTimeWidget(
                date_attrs={"class": "input", "type": "date"},
                time_attrs={"class": "input", "type": "time"}
            ))
    end_time = SplitDateTimeField(widget=SplitDateTimeWidget(
                date_attrs={"class": "input", "type": "date"},
                time_attrs={"class": "input", "type": "time"}
            ))
    
    class Meta:
        model = Rent
        fields = ['start_time', 'end_time']

        
    def clean(self):
        cleaned_data = super().clean()
        tz = get_current_timezone()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        now = datetime.now()

        if end_time < start_time:
            self.add_error(
                "start_time",
                "start date should before end date."
            )
        if start_time < make_aware(now, tz):
            self.add_error(
                "start_time",
                "start date should after now."
            )
        if end_time < make_aware(now, tz):
            self.add_error(
                "end_time",
                "End date should after now."
            )
        return cleaned_data

    




