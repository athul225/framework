from django.urls import path
from . import views

urlpatterns=[
   path('index',views.index),
   path('',views.login),
   path('register',views.register)
]