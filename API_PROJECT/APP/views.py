from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from . serializers import *


# Create your views here.
# def fun(request):
    

#     return JsonResponse({'name':'athul','age':20})

def fun(request):
    if request.method=='GET':
        d=Student.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)