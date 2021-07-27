"""
Creating shortener forms
"""

from django import forms
from . import models

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control", "placeholder": "Input the URL you want shortened"}
    ))

    class Meta:
        model = models.Shortener
        fields = ('long_url',)