from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=10)
    createdAt = models.DateTimeField(name='createdAt',auto_now_add=True)

    class Meta:
        ordering = ('createdAt',)