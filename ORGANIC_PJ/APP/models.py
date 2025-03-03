from django.db import models

# Create your models here.
class User(models.Model):
    name=models.TextField
    email=models.TextField
    uname=models.TextField
    pwd=models.TextField