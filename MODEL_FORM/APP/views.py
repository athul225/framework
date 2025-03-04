from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def model_form(request):
    data=model_forms()
    if request.method=='POST':
        Form=model_forms(request.POST)
        if Form.is_valid():
            Form.save()
    return render(request,'index.html',{'data':data})