from django.db import models

# Create your models here.

class Department(models.Model):
    dname=models.TextField()
    def __str__(self):
        return self.dname

class Students(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    email=models.TextField()
    dname=models.ForeignKey(Department,on_delete=models.CASCADE)