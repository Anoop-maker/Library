
from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    number=models.IntegerField()
    gender=models.CharField(max_length=20)

    def __str__(self):
        return self.name