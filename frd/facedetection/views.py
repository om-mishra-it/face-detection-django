import os
import shutil

import cv2
from django.shortcuts import render
from skimage import io

from .forms import FaceDetectForm
from .models import ImageModel


# Create your views here.
# Method to draw boundary around the detected feature
def draw_boundary(img, scale_factor, min_neighbors, color, text):
    # Converting image to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scale_factor, min_neighbors)
    coordinates = []
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coordinates = [x, y, w, h]
    return coordinates


# Method to detect the features
def detect(img):
    img = io.imread('facedetection/dataset/' + str(img))
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
    coordinates = draw_boundary(img, 1.1, 10, color['blue'], "Face")
    # If feature is detected, the draw_boundary method will return the x,y coordinates and width and height of
    # rectangle else the length of coordinates will be 0
    if len(coordinates) == 4:
        # Updating region of interest by cropping image
        region_of_image = img[coordinates[1]:coordinates[1] + coordinates[3],
                          coordinates[0]:coordinates[0] + coordinates[2]]
        # Passing roi, classifier, scaling factor, Minimum neighbours, color, label text
        # coordinates = draw_boundary(region_of_image, eyeCascade, 1.1, 3, color['red'], "Eye")
        # coordinates = draw_boundary(region_of_image, mouthCascade, 1.1, 5, color['white'], "Mouth")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite('facedetection/dataset/output.jpg', img)
    return img


def get_image(request):
    shutil.rmtree('facedetection/dataset')
    os.mkdir('facedetection/dataset')
    form = FaceDetectForm(request.POST, request.FILES)
    if form.is_valid():
        img = form.cleaned_data.get("img")
        obj = ImageModel.objects.create(img=img)
        obj.save()
        detect(img)

    else:
        form = FaceDetectForm()
    context = {
        'form': form
    }

    return render(request, "frd/get_image.html", context)


def output(request):
    return render(request, "frd/output.html")
