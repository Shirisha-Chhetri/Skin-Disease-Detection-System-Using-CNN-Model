from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='userprofile/', default = 'human.png')

class DiseaseDetail(models.Model):
    name = models.CharField(max_length=50, null=True)
    cause = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_image =  models.URLField(null=True, max_length=1000)
    symptoms = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class DiseaseImage(models.Model):
    existing = models.ForeignKey(DiseaseDetail, default=None, on_delete=models.CASCADE)
    images = models.FileField(blank=True)
    
class SkinCareCenter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    opening_hour = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image =  models.URLField(null=True, blank=True)
    
    def image_tag(self): # new
        return mark_safe('<img src="%s" width="200" height="100" />' % (self.image))

class UserUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='user_uploads/', blank=True)
    