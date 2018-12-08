from django import forms
from .models import given_image

class given_image_form(forms.ModelForm):
    class Meta:
        model=given_image
        fields=['image_given']