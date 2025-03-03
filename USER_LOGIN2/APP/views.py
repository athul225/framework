from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
# Create your views here.

def UserReg(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        uname=request.POST['Username']
        pwd=request.POST['Password']
        cnf_pwd=request.POST['cnf_pwd']
        if cnf_pwd==pwd:
            data=User.objects.create_user(username=uname,email=email,first_name=name,password=pwd)
            data.save()
        else:
            print("passwoed doesn't match")
    return render(request,'register.html')

def UserLogin(request):
    if request.method=='POST':
        uname=request.POST['Username']
        pwd=request.POST['Password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(index)
    return render(request,'login.html')

def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect(UserLogin)
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(UserLogin)
    else:
        return redirect(UserLogin)

    
