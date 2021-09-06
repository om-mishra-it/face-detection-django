from django.db import models


class ImageModel(models.Model):
    img = models.ImageField(upload_to="facedetection/dataset/")

    def __str__(self):
        return self.img.file_data
