from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun),
    path('fun2',views.fun2),
    path('fun3/<d>',views.fun3)
]