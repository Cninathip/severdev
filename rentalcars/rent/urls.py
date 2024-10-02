from django.urls import path
from . import views

urlpatterns = [
    path("", views.TypeCarView.as_view(), name="typecar"),
]