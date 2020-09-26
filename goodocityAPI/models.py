from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.name
