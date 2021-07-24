from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello World")

# Create your views here.
