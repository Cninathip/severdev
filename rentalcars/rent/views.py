from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from rent.models import *
from .forms import *
from django.http import HttpResponse

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request,user)
            return redirect('typecar')  

        return render(request,'login.html', {"form":form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    

class TypeCarView(View):
    def get(self, request):
        types = VehicleType.objects.order_by("id")

        return render(request, "typecar.html", {
            "types": types
        })
    

class TypeCarAdd(View):
    def get(self, request):
        form = VehicleTypeForm()
        return render(request, "formtypecar.html", {
            "form": form,
        })

    def post(self, request):
        form = VehicleTypeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('typecar-list')

        return render(request, "formtypecar.html", {
            "form": form
        })
    

class TypeCarUpdate(View):
    def get(self, request, pk):
        typecar = VehicleType.objects.get(pk=pk)
        form = VehicleTypeForm(instance=typecar)
        return render(request, "formtypecar.html", {
            "form": form,
        })

    def post(self, request, pk):
        typecar = VehicleType.objects.get(pk=pk)
        form = VehicleTypeForm(request.POST, request.FILES, instance=typecar)

        if form.is_valid():
            form.save()
            return redirect('typecar-list')

        return render(request, "formtypecar.html", {
            "form": form
        })


class TypeCarDelete(View):
    def get(self, request, pk):
        typecar = VehicleType.objects.get(pk=pk)
        typecar.delete()
        return redirect("typecar-list")


class CarView(View):
    def get(self, request, pk):
        cars = Vehicle.objects.filter(type=pk)

        return render(request, "car.html", {
            "cars": cars
        })


class EmployeeView(View):
    def get(self, request):
        types = VehicleType.objects.order_by("id")

        return render(request, "employee.html", {
            "types": types
        })