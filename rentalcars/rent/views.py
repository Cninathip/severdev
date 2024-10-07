
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from rent.models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import make_aware, get_current_timezone
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect

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
        typecar = VehicleType.objects.get(pk=pk)
        search_date = request.GET.get("search_date")
        search_time = request.GET.get("search_time")
        tz = get_current_timezone()
        
        if search_date and search_time:
            search_datetime = timezone.datetime.strptime(f"{search_date} {search_time}", "%Y-%m-%d %H:%M")
            search_datetime = make_aware(search_datetime, tz)
        else:
            now = datetime.now()
            search_datetime = make_aware(now, tz)

        print(search_datetime)
        cars = Vehicle.objects.filter(type=pk).exclude(
            rent__start_time__lte=search_datetime,
            rent__end_time__gte=search_datetime
        )

        return render(request, "car.html", {
            "cars": cars,
            "search_date": search_date,
            "search_time": search_time,
            "pk": pk,
            "typecar": typecar,
        })
    

class CarAdd(View):
    def get(self, request, pk):
        form = VehicleForm()
        return render(request, "formcar.html", {
            "form": form,
            "pk":pk
        })
    
    def post(self, request, pk):
        form = VehicleForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('car-list', pk=pk)

        return render(request, "formcar.html", {
            "form": form,
            "pk":pk
        })




class EmployeeView(View):
    def get(self, request):
        search = request.GET
        emp = Employee.objects.all().order_by("id")
        form = EmployeeForm(request.POST)

        if search.get("search"):
            emp = Employee.filter(
                # first_name__icontains=search.get("search"),
                id__icontains=search.get("search")
            )

        return render(request, "employee.html", {
            "emp": emp,
            "form": form
        })
    
    def post(self, request):
        emp = Employee.objects.all().order_by("id")
        form = EmployeeForm(request.POST)        

        if form.is_valid():
            form.save()
            return redirect('typecar-list')

        return render(request, "employee.html", {
            "emp": emp,
            "form": form
        })