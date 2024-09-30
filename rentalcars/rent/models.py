from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    total_cost = models.IntegerField()
    create_at = models.DateTimeField()
    pay_at = models.DateTimeField()
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
        return self.name
    

class Detail(models.Model):
    insurance = models.CharField(max_length=100)
    price_per_hour = models.IntegerField()
    price_per_day = models.IntegerField()
    seat = models.IntegerField()
    price_per_hour = models.CharField()

    def __str__(self):
        return self.name


class Vehicle_type(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    type = models.ForeignKey(Vehicle_type, on_delete=models.PROTECT)
    vehicle_number = models.CharField(max_length=10)
    vehicle_status = models.BooleanField()
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
    



