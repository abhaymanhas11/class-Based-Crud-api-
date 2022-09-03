from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    address=models.CharField(max_length=100)

