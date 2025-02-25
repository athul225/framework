from django.urls import path
from . import views

urlpatterns = [
   path('register',views.UserReg),
   path('',views.UserLogin),
   path('index',views.index)
    
]