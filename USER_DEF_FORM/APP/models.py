from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField()
    name=models.TextField()
    mark=models.IntegerField()