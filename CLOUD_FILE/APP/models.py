from django.db import models

# Create your models here.

class User(models.Model):
    name=models.TextField()
    email=models.TextField()
    pwd=models.TextField()
    
    
    
class Files(models.Model):
    doc=models.FileField()
    des=models.TextField()