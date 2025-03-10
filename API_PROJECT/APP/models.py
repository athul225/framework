from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField()
    roll=models.IntegerField()
    place=models.TextField()

    def __str__(self):
        return self.name