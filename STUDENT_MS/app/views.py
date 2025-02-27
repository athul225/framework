from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    dnames=Department.objects.all()
    if request.method=='POST':
        name=request.POST['Name']
        age=request.POST['Age']
        email=request.POST['Email']
        dpk=request.POST['dname']
        dname=Department.objects.get(pk=dpk)
        data=Students.objects.create(name=name,age=age,email=email,dname=dname)
        data.save()

    return render(request,'index.html',{'dnames':dnames})
