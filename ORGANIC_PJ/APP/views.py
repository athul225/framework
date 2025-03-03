from django.shortcuts import render,redirect

# Create your views here.
def index(request):

    

    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        uname=request.POST['Username']
        pwd=request.POST['Password']
        cnf_pwd=request.POST['cnf_pwd']
        if cnf_pwd==pwd:
            data=User.objects.create(name=name,email=email,uname=uname,pwd=pwd)
            data.save()
        else:
            print("password doesn't match")
    return render(request,'register.html')

def login(request):

    if request.method=='POST':
            uname=request.POST['uname']
            pwd=request.POST['password']
            user=User.authenticate(username=uname,password=pwd)
            if user is not None:
                User.login(request,user)
                return redirect(index)
            
    return render(request,'login.html')