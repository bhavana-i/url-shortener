"""
Creating shortener forms
"""

from django import forms
from . import models

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Input the URL you want to shorten"}
    ))

    class Meta:
        model = models.Shortener
        fields = ('long_url',)