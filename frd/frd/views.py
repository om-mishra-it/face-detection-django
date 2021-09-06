from django.shortcuts import render
import cv2
# from .models import ImageUpload


# Create your views here.
# Method to draw boundary around the detected feature
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    # Converting image to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coordinates = []
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coordinates = [x, y, w, h]
    return coordinates


# Method to detect the features
def detect(img, face_cascade, eyeCascade, mouthCascade):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
    coordinates = draw_boundary(img, face_cascade, 1.1, 10, color['blue'], "Face")
    # If feature is detected, the draw_boundary method will return the x,y coordinates and width and height of
    # rectangle else the length of coordinates will be 0
    if len(coordinates) == 4:
        # Updating region of interest by cropping image
        roi_img = img[coordinates[1]:coordinates[1] + coordinates[3], coordinates[0]:coordinates[0] + coordinates[2]]
        # Passing roi, classifier, scaling factor, Minimum neighbours, color, label text
        # coordinates = draw_boundary(roi_img, eyeCascade, 1.1, 3, color['red'], "Eye")
        # coordinates = draw_boundary(roi_img, mouthCascade, 1.1, 5, color['white'], "Mouth")
    return img


def home(request):
    # context = {'form': ImageUpload()}
    # return render(request, "frd/base.html", context)
    pass