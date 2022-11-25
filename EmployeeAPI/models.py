from django.db import models

# Create your models here.
class Employee(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Designation=models.CharField(max_length=100)

 