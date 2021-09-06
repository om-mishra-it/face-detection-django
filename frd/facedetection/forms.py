from django import forms


class FaceDetectForm(forms.Form):
    img = forms.ImageField()
