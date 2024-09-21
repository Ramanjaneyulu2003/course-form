from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=50)
    scourse=models.CharField(max_length=50)
    sfees=models.IntegerField()