"""
URL configuration for rentalcars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rent.views import Login, Logout, Register
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("register/", Register.as_view(), name="register"),
    path('rent/', include("rent.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #ช่วยชี้ไปที่ไฟล์ที่เก็บไว้ใน media ตอนเรียก .url