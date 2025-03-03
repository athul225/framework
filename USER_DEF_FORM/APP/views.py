from django.shortcuts import render
from . forms import *
from .models import *

# Create your views here.

def user_form(request):
    data=user_forms()
    if request.method=='POST':
        Form=user_forms(request.POST)
        if Form.is_valid():
            Roll=Form.cleaned_data['roll']
            Name=Form.cleaned_data['name']
            Mark=Form.cleaned_data['mark']
            data1=Student.objects.create(roll=Roll,name=Name,mark=Mark)
            data1.save()
            

    return render(request,'index.html',{'data':data})