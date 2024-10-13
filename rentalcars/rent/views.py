
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from rent.models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import make_aware, get_current_timezone
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request,user)
            return redirect('typecar-list')  

        return render(request,'login.html', {"form":form})


class Logout(View):
    login_url = "/login/"
    def get(self, request):
        logout(request)
        return redirect('login')
    

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                first_name = form.cleaned_data["first_name"],
                last_name = form.cleaned_data["last_name"],
                email = form.cleaned_data["email"],
                phone_number = request.POST.get("phone_number")
            )

            login(request, user)
            return redirect('typecar-list')
        return render(request, 'register.html', {"form": form})
    
class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, "changepassword.html", {"form": form})
    
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        old_password: str = request.POST.get("old_password")
        new_password: str = request.POST.get('new_password')
        confirm_password: str = request.POST.get('confirm_password')
        if not request.user.check_password(old_password):
            messages.warning(request, "old password doesn't match.")
            return redirect("change_password")
        if old_password == new_password:
            messages.warning(request, "your new password cannot be the same as your old password.")
            return redirect("change_password")
        if new_password != confirm_password:
            messages.warning(request, "new password doesn't match.")
            return redirect("change_password")
        
        request.user.set_password(new_password)
        request.user.save()
        messages.success(request, "password change successfull. your new password would take effect on next login.")
        return redirect("profile")

class TypeCarView(LoginRequiredMixin, View):
    login_url = "/login/"
    
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
            search_datetime = datetime.strptime(f"{search_date} {search_time}", '%Y-%m-%d %H:%M')
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
    def post(self, request, pk):
        car = Vehicle.objects.get(pk=pk)
        return render(request, "cardetail.html"),{
            "car": car
        }
    
class CarDetailView(View):
    def get(self, request, pk):
        car = Vehicle.objects.get(pk=pk)
        form = RentForm()
        context = {"car": car, "form": form}
        return render(request, "cardetail.html", context)
    
    def post(self, request, pk):
        form = RentForm(request.POST)
        car = Vehicle.objects.get(pk=pk)
        if form.is_valid():
            pay = Payment(
                total_cost = 1,
                pay_status = False
            )
            pay.save()
            rent = Rent(
                customer = Customer.objects.get(
                    first_name = request.user.first_name
                    , last_name = request.user.last_name
                    , email = request.user.email
                ),
                vehicle = Vehicle.objects.get(pk=pk),
                payment = pay,
                start_time = form.cleaned_data["start_time"],
                end_time = form.cleaned_data["end_time"],
                return_status = False
            )
            rent.save()
            return redirect("profile")
        return render(request, "cardetail.html", {"car": car, "form": form})
    
class CarEditView(View):
    def get(self, request, pk):
        car = Vehicle.objects.get(pk=pk)
        form = VehicleForm(instance=car)
        return render(request, "formcar.html", {
            "form": form,
            "pk":pk
        })
    
    def post(self, request, pk):
        car = Vehicle.objects.get(pk=pk)
        form = VehicleForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()
            return redirect('car-detail', pk=pk)

        return render(request, "formcar.html", {
            "form": form,
            "pk":pk
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
        query = request.GET
        emp = Employee.objects.all().order_by("id")
        form = EmployeeForm()

        if query.get("search"):
            emp = emp.filter(
                Q(id__icontains=query.get("search"))|
                Q(first_name__icontains=query.get("search"))
            )

        return render(request, "employee.html", {
            "emp": emp,
            "form": form
        })
    
    def post(self, request):
        form = EmployeeForm(request.POST)   
        emp = Employee.objects.all().order_by("id")

        if form.is_valid():
            form.save()
            return redirect('employee')

        return render(request, "employee.html", {
            "emp": emp,
            "form": form
        })
    
class ProfileView(View):
    def get(self, request):
        query = request.GET
        rent = Rent.objects.all()
        
        if query.get("search"):
            rent = rent.filter(
                Q(vehicle__name__icontains=query.get("search"))|
                Q(vehicle__number__icontains=query.get("search"))
            )

        return render(request, "profile.html", {"rent": rent})
    
class RentApprove(View):
    def get(self, request, pk):
        rent = Rent.objects.get(pk=pk)
        rent.return_status = True
        rent.save()

        return redirect("profile")
    
class RentCancle(View):

    def get(self, request, pk):
        rent = Rent.objects.get(pk=pk)
        rent.delete()

        return redirect("profile")