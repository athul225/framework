from rest_framework import serializers
from . models import *


# class sample(serializers.Serializer):
#     name=serializers.CharField()
#     roll=serializers.IntegerField()
#     place=serializers.CharField()

class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'