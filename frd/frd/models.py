from django.db import models
from django import forms


# Create your models here.
class ImageUpload(forms.Form):
    img = models.ImageField(upload_to="image/")
