"""
URL configuration for project project.

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1),
    path('hai',views.fun2),
    path('detail/<name>/<int:age>',views.fun3),
    path('largest/<int:a>/<int:b>/<int:c>',views.fun4),
    path('data/<c>',views.sample),
    path('index',views.index),
    path('student',views.student),
    path('bike',views.cost),
    path('salary',views.salary),
    path('unit',views.current),
    path('divisible',views.divide)
]
