from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from . serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins


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
    
@api_view(['GET','POST'])
def fun4(request):
    
    if request.method=='GET':
        d=Student.objects.all()
        s=model_serializers(d,many=True)
        return Response(s.data)

    elif request.method=='POST':
        s=model_serializers(data=request.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST','PUT','DELETE'])
def fun5(request,d):
    
    try:
        demo=Student.objects.get(pk=d)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        s=model_serializers(demo)
        return Response(s.data)
    elif request.method=='PUT':
        s=model_serializers(demo,data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class fun6(APIView):
    def get(self,request):
        demo=Student.objects.all()
        s=model_serializers(demo,many=True)
        return Response(s.data)
    def post(self,request):
        s=model_serializers(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class fun7(APIView):
    def get(self,request,d):
        try:
            demo=Student.objects.get(pk=d)
            s=model_serializers(demo)
            return Response(s.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,d):
        try:
            demo=Student.objects.get(pk=d)
            s=model_serializers(demo,data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,req,d):
        
        try:
            demo=Student.objects.get(pk=d)
            demo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class genericapiview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=model_serializers
    queryset=Student.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


class update(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=model_serializers
    queryset=Student.objects.all()
    lookup_field='id'
    def get(self,request):
        return self.list(request)
    def put(self,request,id):
        return self.create(request,id)
    def delete(self,request,id):
        return self.create(request,id)
    