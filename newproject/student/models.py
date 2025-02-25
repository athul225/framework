from django.db import models

# Create your models here.

class students(models.Model):
    adm_no=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.TextField()
    clas=models.IntegerField()
    course=models.TextField()