from django.contrib import admin
from .models import Profile, DiseaseDetail, SkinCareCenter, AffectedImage, DiseaseImage
# Register your models here.

class ImageAdmin(admin.StackedInline):
    model = DiseaseImage
 
@admin.register(DiseaseDetail)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
 
    class Meta:
       model = DiseaseDetail
 
@admin.register(DiseaseImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["existing", "images"]


class userUploadedPhoto(admin.ModelAdmin):
    list_display = ["user", "image"]

admin.site.register(AffectedImage, userUploadedPhoto)
admin.site.register(Profile, userUploadedPhoto)

class careCenterImage(admin.ModelAdmin):
    list_display = ["name", "image_tag", "location"]

admin.site.register(SkinCareCenter,careCenterImage)
