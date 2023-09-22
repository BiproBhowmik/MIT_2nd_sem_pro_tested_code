from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=100)
