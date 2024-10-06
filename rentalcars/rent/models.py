from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Payment(models.Model):
    total_cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    pay_at = models.DateTimeField(null=True)
    pay_status = models.BooleanField()

    def __str__(self):
        return self.name
    

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Detail(models.Model):
    insurance = models.CharField(max_length=100)
    price_per_hour = models.IntegerField()
    price_per_day = models.IntegerField()
    seat = models.IntegerField()
    description = models.CharField()

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='type/', blank=True, null=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    vehicle_status = models.BooleanField()
    vehicle_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    detail = models.ForeignKey(Detail, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

class Rent(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    return_status = models.BooleanField()

    def __str__(self):
        return self.name
    



