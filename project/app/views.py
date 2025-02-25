from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return HttpResponse("welcome to all")
def fun2(req):
    return HttpResponse("hello")
def fun3(req,name,age):
    return HttpResponse(name+str(age))
def fun4(req,a,b,c):
    if(a>b):
        if(a>c):
            return HttpResponse("largest: "+str(a))
        else:
             return HttpResponse("largest: "+str(c))
    else:
        if(b>c):
             return HttpResponse("largest: "+str(b))
        else:
             return HttpResponse("largest: "+str(c))
def sample(request,c):
    a={'name':'athul','age':20}
    b=c
    return render(request,'sample.html',{'data':a,'data1':b})


l=[{'name':'athul','age':22},{'name':'amal','age':22},{'name':'akhil','age':22}]
def index(request):
    if request.method=='POST':
        # print(request.POST)
        name=request.POST['name']
        age=request.POST.get('age')
        print(name,age)
        l.append({'name':name,'age':age})
        return redirect(index)
        
    
    return render(request,'index.html',{'data':l})


age_gt_20=[]
age_lt_20=[]
def student(request):
    if request.method=='POST':
        name=request.POST['name']
        age=int(request.POST.get('age'))
        # print(age,type(age))
        if age >= 20:
            print(name,age)
            age_gt_20.append({'name':name,'age':age})
            return redirect(student)
        elif age <20:
            print(name,age)
            age_lt_20.append({'name':name,'age':age})
            return redirect(student)
            
            
        
    
    return render(request,'student.html',{'data':age_gt_20,'data1':age_lt_20})


def cost(request):
    b=0
    if request.method =='POST':
        value=int(request.POST['cat'])
        if(value > 100000):
            b=value * 0.15          
            return redirect(cost)
        elif(value <= 100000 and value>50000):
            b=value * 0.10          
            
        else:
            b=value * 0.05
             
    return render(request,'bike.html',{'tax':b})


def salary(request):
    b=0
    if request.method=='POST':
        sal=int(request.POST['salary'])
        ser=int(request.POST['services'])
        if(ser>5):
            b=0.05 * sal
    
    return render(request,'salary.html',{'salary':b})


def current(request):
    b=0
    if request.method=='POST':
        power=int(request.POST['unit'])
        if power<=100:
            b="no charge"
        elif power<=200:
            b=(power-100)*5
        else:
            b=(power-200)*10+500
            
    return render(request,'current.html',{'data':b})

def divide(request):
    c=0
    if request.method=='POST':
        a=int(request.POST['divisible'])
        b=(a%10)
        if b%3==0:
            c="no. is divisible by 3"
        else:
            c="no. is not divisible by 3"
    return render(request,'divisible.html',{'data':c})
    