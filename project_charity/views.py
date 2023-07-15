from django.shortcuts import render
from django.conf import settings
from .models import *


def home(request):
    about = About_us_mainpaig.objects.all()
    context = {"about": about,}
    return render(request, 'index.html', context )

def about(request):
    return render(request, 'about.html', )


def causes(request):
    return render(request, 'causes.html', )

def causes_single(request):
    return render(request, 'causes_single.html', )

def gallery(request):
    return render(request, 'gallery.html', )


def contact(request):
    return render(request, 'contact.html', )



