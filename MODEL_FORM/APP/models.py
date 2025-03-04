from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=200)
    mark=models.IntegerField()