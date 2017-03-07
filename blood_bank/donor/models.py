from django.db import models

# Create your models here.

class Donor(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    bloodGroup = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    createdAt = models.DateTimeField('createdAt',auto_now_add=True)