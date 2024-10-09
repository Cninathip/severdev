from django.urls import path
from . import views

urlpatterns = [
    path("", views.TypeCarView.as_view(), name="typecar-list"),
    path("typecar", views.TypeCarAdd.as_view(), name="typecar-add"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("profile/changepassword", views.ChangePasswordView.as_view(), name="changepassword"),
    path("typecar-delete/<int:pk>", views.TypeCarDelete.as_view(), name="typecar-delete"),
    path("typecar-update/<int:pk>", views.TypeCarUpdate.as_view(), name="typecar-update"),
    path("<int:pk>", views.CarView.as_view(), name="car-list"),
    path("detail/<int:pk>", views.CarDetailView.as_view(), name="car-detail"),
    path("detail/<int:pk>/edit", views.CarEditView.as_view(), name="car-edit"),
    path("<int:pk>/car-add", views.CarAdd.as_view(), name="car-add"),
    path("employee", views.EmployeeView.as_view(), name="employee"),
]