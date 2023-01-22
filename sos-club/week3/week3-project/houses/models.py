from django.db import models

# Create your models here.

class House(models.Model):
    """ Model definition for Houses"""
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=100)


class Todo(models.Model):
    """ Model definition for Todo"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_starred = models.BooleanField()