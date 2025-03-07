
from django.shortcuts import render,redirect
from .models import * 

# Create your views here.
def index(request):
    


    return render(request,'index.html')



def register(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        pwd=request.POST['Password']
        cnf_pwd=request.POST['cnf_pwd']
        if cnf_pwd==pwd:
            data=User.objects.create(name=name,email=email,pwd=pwd)
            data.save()
        else:
            print("password doesn't match")
    
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['Email']
        pwd=request.POST['pwd']
        
        try:
            data=User.objects.get(pwd=pwd,email=email)
            request.session['user']=email
            return redirect(index)
            
        except:
            print('Not found')
            return redirect(login)
    
    return render(request,'login.html')

def upload(request):
    docs=Files.objects.all()
    if request.method=='POST':
        doc=request.FILES['doc']
        des=request.POST['des']
        data=Files.objects.create(doc=doc,des=des)
        data.save()
        return redirect(index)
    return render(request,'upload.html',{'docs':docs})

   