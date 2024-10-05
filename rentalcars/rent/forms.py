from django import forms
from .models import VehicleType

class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = ['name', 'description', 'image']