from django import forms
from .models import File


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# data accessible > 'request.FILES['file']'
