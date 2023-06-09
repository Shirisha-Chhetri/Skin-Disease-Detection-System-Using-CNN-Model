from django.contrib import admin
from .models import Profile, DiseaseDetail, SkinCareCenter

# Register your models here.

admin.site.register(Profile)
admin.site.register(DiseaseDetail)
admin.site.register(SkinCareCenter)