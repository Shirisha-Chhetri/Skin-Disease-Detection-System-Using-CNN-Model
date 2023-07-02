from django.db import models
from django.contrib.auth.models import User
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
    def __str__(self):
        return f'{self.user}'


class DiseaseDetail(models.Model):
    name = models.CharField(max_length=50, null=True)
    cause = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images =  models.URLField(null=True, max_length=1000)
    image = models.ImageField(blank=True)
    symptoms = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class SkinCareCenter(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    mail = models.CharField(max_length=100, null=True, blank=True)
    opening_hour = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image =  models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class AffectedImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='affectedphoto/')
    def __str__(self):
        return f'{self.user}'