from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=800)
    status = models.ForeignKey('Status')
    project = models.ForeignKey('Project', blank=True, null=True, on_delete=models.SET_NULL)
    
class Status(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=120)
    order = models.IntegerField(default=0, blank=True)
    url_path = models.SlugField()
    
# class Settings(models.Model):
#     name = models.CharField(max_length=255,)