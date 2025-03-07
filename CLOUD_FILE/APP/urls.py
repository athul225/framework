from django.urls import path
from . import views
urlpatterns=[
   path('index',views.index),
   path('register',views.register),
   path('',views.login),
   path('upload',views.upload)
]