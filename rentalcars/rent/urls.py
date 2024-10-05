from django.urls import path
from . import views

urlpatterns = [
    path("", views.TypeCarView.as_view(), name="typecar-list"),
    path("typecar", views.TypeCarAdd.as_view(), name="typecar-add"),
    path("typecar-delete/<int:pk>", views.TypeCarDelete.as_view(), name="typecar-delete"),
    path("typecar-update/<int:pk>", views.TypeCarUpdate.as_view(), name="typecar-update"),
    path("<int:pk>", views.CarView.as_view(), name="car-list"),
    path("employee", views.EmployeeView.as_view(), name="employee"),
]