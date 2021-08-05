"""
URLs for the urlreduce app
"""

from django.urls import path
from .views import home_view, redirect_url_view

from . import views

urlpatterns = [
    path("", home_view, name="home"),
    path('<str:shortened_url>', redirect_url_view, name='redirect'),
]

