from django.contrib import admin
from .models import Profile, DiseaseDetail, SkinCareCenter, DiseaseImage, UserUpload

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
    pass
    list_display = ["existing", "images"]

class userUploadedPhoto(admin.ModelAdmin):
    list_display = ["user", "image"]

admin.site.register(Profile, userUploadedPhoto)
admin.site.register(UserUpload, userUploadedPhoto)


class careCenterImage(admin.ModelAdmin):
    list_display = ["name", "image_tag", "location"]

admin.site.register(SkinCareCenter,careCenterImage)
    