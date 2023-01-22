from django.db import models

# Create your models here.

class TodoModel(models.Model):
    """ Model definition for Todo"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_starred = models.BooleanField()
    create_time = models.DateTimeField(verbose_name = '작성일', blank = True)
    modified_time = models.DateTimeField(verbose_name = '수정일', blank = True)