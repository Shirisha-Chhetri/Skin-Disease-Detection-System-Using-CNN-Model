from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='userprofile', default = 'human.png')

    def __str__(self):
        return f'{self.user}'


class DiseaseDetail(models.Model):
    name = models.CharField(max_length=50, null=True)
    cause = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images =  models.URLField(null=True)
    symptoms = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class SkinCareCenters(models.Model):
    name = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=True, null=True)
    image =  models.URLField(null=True)
    
    def __str__(self):
        return self.name