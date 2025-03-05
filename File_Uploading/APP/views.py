from django.shortcuts import render,redirect
from .models import * 

# Create your views here.
def index(request):
    docs=Files.objects.all()
    if request.method=='POST':
        doc=request.FILES['doc']
        des=request.POST['des']
        data=Files.objects.create(doc=doc,des=des)
        data.save()
        return redirect(index)
    return render(request,'index.html')
def register(request):



    return render(request,'register.html')

def login(request):


    return render(request,'login.html')