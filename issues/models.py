from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=800)
    status = models.ForeignKey('Status')
    
class Status(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()
