from django import forms

#csv file upload garne
class UploadForm(forms.Form):
    uploadfile = forms.FileField()