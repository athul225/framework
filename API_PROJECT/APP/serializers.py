from rest_framework import serializers


class sample(serializers.Serializer):
    name=serializers.CharField()
    roll=serializers.IntegerField()
    place=serializers.CharField()
