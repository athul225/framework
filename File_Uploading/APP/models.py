from django.db import models

# Create your models here.
class Files(models.Model):
    doc=models.FileField()
    des=models.TextField()