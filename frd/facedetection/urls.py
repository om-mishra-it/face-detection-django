from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_image),
    path('output', views.output, name="output")
]
