from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe 
from cryptography.fernet import Fernet

# Create your models here.

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# write_key()
key = load_key()
file = "media/userprofile"

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

    def __str__(self):
        return self.existing
 
    
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
    
class AffectedImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='affectedphoto/')
    