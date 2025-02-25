from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
l=[]
def student(request):
    datas=students.objects.all()
    print(datas)
    if request.method=='POST':
        a=int(request.POST['id'])
        b=request.POST['name']
        c=int(request.POST['age'])
        d=request.POST['email']
        e=int(request.POST['class'])
        f=request.POST['course']
        data=students.objects.create(adm_no=a,name=b,age=c,email=d,clas=e,course=f)
        data.save()
        # print(id,name,age,email,clas,course)
        # l.append({'id':a,'name':b,'age':c,'email':d,'class':e,'course':f})
        return redirect(student)
    
    return render(request,'student.html',{'datas':datas})


def update(request,pk):
    data1=students.objects.get(pk=pk)
    print(data1)
    if request.method=='POST':
        a=int(request.POST['id'])
        b=request.POST['name']
        c=int(request.POST['age'])
        d=request.POST['email']
        e=int(request.POST['class'])
        f=request.POST['course']
        students.objects.filter(pk=pk).update(adm_no=a,name=b,age=c,email=d,clas=e,course=f)
        return redirect(student)
                
    
    return render(request,'update.html',{'data1':data1})

def delete(request,pk):
    students.objects.filter(pk=pk).delete()
    return redirect(student)


l=[]
def management(request):
    datas=students.objects.all()
    print(datas)
    if request.method=='POST':
        a=int(request.POST['id'])
        b=request.POST['name']
        c=int(request.POST['age'])
        d=request.POST['email']
        e=int(request.POST['class'])
        f=request.POST['course']
        data=students.objects.create(adm_no=a,name=b,age=c,email=d,clas=e,course=f)
        data.save()
        # print(id,name,age,email,clas,course)
        # l.append({'id':a,'name':b,'age':c,'email':d,'class':e,'course':f})
        return redirect(student)
    
    return render(request,'student.html',{'datas':datas})
