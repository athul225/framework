from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from . serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def fun(request):
    

#     return JsonResponse({'name':'athul','age':20})

def fun(request):
    if request.method=='GET':
        d=Student.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)

@csrf_exempt
def fun2(request):
    if request.method=='GET':
        d=Student.objects.all()
        s=model_serializers(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif request.method=='POST':
        d=JSONParser().parse(request)
        s=model_serializers(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.data)
        

@csrf_exempt
def fun3(request,d):
    try:
        demo=Student.objects.get(pk=d)
    except:
        return HttpResponse("Invalid")
    if request.method=='GET':
        s=model_serializers(demo)
        print(s.data)
        return JsonResponse(s.data)
    elif request.method=='PUT':
        d=JSONParser().parse(request)
        s=model_serializers(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif request.method=='DELETE':
        demo.delete()
        return JsonResponse("Deleted")